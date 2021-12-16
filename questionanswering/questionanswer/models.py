from django.db import models
from ..topic.models import Topic


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    class Meta:
        abstract = False  # To make an abstract base class that inherits from another abstract base class


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    is_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    def is_answers(self):
        return self.is_answer

    class Meta:
        abstract = False


class Score(models.Model):
    score = models.PositiveIntegerField(default=0)
    minute = models.PositiveIntegerField(default=0)
    second = models.PositiveIntegerField(default=0)
    previous_time_minute = models.PositiveIntegerField(default=0)
    previous_time_second = models.PositiveIntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        return "Score = {} ".format(self.score)

    def is_time_up(self):
        if self.minute == 0 and self.second == 0:
            return True
        else:
            return False

    # convert Score model to be singleton.
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def get_query_score(self):
        return self.score

    class Meta:
        abstract = False
