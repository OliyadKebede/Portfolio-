from django.db import models
from datetime import datetime
from django.urls import reverse
from math import fabs
from ..utility.utilities import change_to_minute_second


class Topic(models.Model):
    title = models.CharField(max_length=100)
    given_time_in_minute = models.PositiveIntegerField('given time')
    pub_date = models.DateTimeField('date published', default=datetime.now)

    def query_question_length(self):
        return len(self.question_set.all())

    def get_absolute_url(self):
        return reverse('Topic:check_index')

    def check_time(self, scores):
        starting_point = self.given_time_in_minute
        print("starting_point :", starting_point)

        previous_time_in_minute = scores.minute
        previous_time_in_second = scores.second
        if previous_time_in_minute == 0 and previous_time_in_second == 0:

            starting_minute = starting_point - 1
            starting_second = 60

            scores.date = datetime.now()

            scores.minute = starting_minute
            scores.second = starting_second
            scores.previous_time_minute = 1
            scores.previous_time_second = 1
            scores.save()


        else:

            print(scores.date)
            print(datetime.now())
            test = scores.date.replace(tzinfo=None)
            print(datetime.now() - test)

            now_time = datetime.now()
            distance = now_time - test
            seconds = distance.seconds
            minute, second = change_to_minute_second(seconds=seconds)

            new_time_in_minute = scores.minute - minute
            new_time_in_second = scores.second - second

            if new_time_in_second > 0  :
                scores.minute = int(fabs(new_time_in_minute))
                scores.second = new_time_in_second
                scores.date = now_time
                scores.save()
            else:
                scores.date = now_time
                scores.minute = 0
                scores.second = 0
                scores.save()


    # finished time in minute count until a given minute is finished

    def __str__(self):
        return self.title

    class Meta:
        abstract = False
