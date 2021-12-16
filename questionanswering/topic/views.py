# class based view
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from ..utility.utilities import calculate
from .models import Topic
from ..questionanswer.models import Score
from django.views.generic import CreateView, UpdateView
from django.views.generic import DetailView, ListView


class TopicListView(ListView):
    model = Topic
    template_name = 'topic/topicindex.html'
    context_object_name = 'topic_lists'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic/detail.html'


class TopicResultDetailView(DetailView):
    model = Topic

    def get(self, request, *args, **kwargs):
        # Handles display result of the Topic object
        score1 = get_object_or_404(Score, id=1)
        self.object = self.get_object()
        score = score1
        user_score = score.score
        question_length = self.object.query_question_length()
        remark = calculate(user_score, question_length)
        Score.objects.filter(id=1).update(score=0, minute=0, second=0,
                                          previous_time_minute=0, previous_time_second=0
                                          )

        return render(request, 'topic/total_result.html', {'score': score, 'topic': self.object, 'remark': remark})


class TopicCreateViewForm(CreateView):
    model = Topic
    fields = ['title', 'given_time_in_minute', 'pub_date']
    context_object_name = 'add_topic'
    template_name = 'topic/new_topic.html'


class TopicTimeUpdate(UpdateView):
    model = Topic
    fields = ['given_time_in_minute']
    context_object_name = 'add_topic'
    template_name = 'topic/update_topic_time.html'

    def get_success_url(self):
        return reverse('Topic:topic_welcome', args=(self.object.pk,)
                       )
