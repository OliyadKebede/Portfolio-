from django import forms

ANSWER_CHOICE = [
    ('ch1', 'Choice 1'),
    ('ch2', 'Choice 2'),
    ('ch3', 'Choice 3'),
    ('ch4', 'Choice 4'),
]


class AddQuestionForm(forms.Form):
    question = forms.CharField(label="Question", max_length=100)
    choice_1 = forms.CharField(label="choice 1", max_length=50)
    choice_2 = forms.CharField(label="choice 2", max_length=50)
    choice_3 = forms.CharField(label="choice 3", max_length=50)
    choice_4 = forms.CharField(label="choice 4", max_length=50)
    choices_answer = forms.ChoiceField(required=True, choices=ANSWER_CHOICE )
