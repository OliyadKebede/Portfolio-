from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..topic.models import Topic
from .forms import AddQuestionForm
from .models import Score


# try using decoration functions
def questions_page(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    scores = Score.objects.get(id=1)
    topic.check_time(scores)
    questions = topic.question_set.all()

    if scores.second == 0 or not questions:
        score = scores
        Score.objects.filter(id=1).update(score=0, minute=0, second=0,
                                          previous_time_minute=0, previous_time_second=0
                                          )

        return render(request, 'question_answer/sorry.html', {'topic': topic, 'score': score})
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    if request.GET.get('page') is not None:

        c = request.GET.get('choice')

        try:
            num = page_obj.previous_page_number()
            page_obj = paginator.get_page(num)
            question = page_obj.object_list
            q = question[0]
            selected_choice = q.choice_set.get(pk=int(c))

            if selected_choice.is_answers():
                scores.score += 1
                scores.save()

            num = page_obj.next_page_number()
            page_obj = paginator.get_page(num)

        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)
            question = page_obj.object_list
            q = question[0]
            if c == '':
                return render(request, 'question_answer/question_pages.html',
                              {'page_obj': page_obj, 'topic': topic,
                               'error_message': "You didn't select a choice.",
                               'score': scores
                               })

            selected_choice = q.choice_set.get(pk=int(c))

            if selected_choice.is_answers():
                scores.score += 1
                scores.save()
            #
            return HttpResponseRedirect(reverse('Topic:total_result', args=(topic.id,)))


        except (ValueError, Choice.DoesNotExist):

            # Redisplay the question  form.
            return render(request, 'question_answer/question_pages.html', {'page_obj': page_obj, 'topic': topic,
                                                                           'error_message': "You didn't select a choice.",
                                                                           'score': scores
                                                                           })

    return render(request, 'question_answer/question_pages.html',
                  {'page_obj': page_obj, 'topic': topic, 'score': scores})


def new_question(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddQuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            question_text = form.cleaned_data['question']
            choice1 = form.cleaned_data['choice_1']
            choice2 = form.cleaned_data['choice_2']
            choice3 = form.cleaned_data['choice_3']
            choice4 = form.cleaned_data['choice_4']
            answer_choice = form.cleaned_data['choices_answer']

            topic.question_set.create(question_text=question_text)
            question = topic.question_set.last()

            answer = {'ch1': choice1, 'ch2': choice2, 'ch3': choice3, 'ch4': choice4}
            file = zip(answer.values(), answer.keys())

            for value, key in file:
                if key == answer_choice:
                    question.choice_set.create(choice_text=value, is_answer=True)
                else:
                    question.choice_set.create(choice_text=value, is_answer=False)

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:

        return HttpResponseRedirect(reverse('QA:results', args=(topic.id,)))
        # if a GET (or any other method) we'll create a blank form

    else:
        form = AddQuestionForm()

    return render(request, 'question_answer/newQuestion.html', {'form': form, 'topic': topic})


def results(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    question = topic.question_set.last()
    return render(request, 'question_answer/results.html', {'question': question, 'topic': topic})
