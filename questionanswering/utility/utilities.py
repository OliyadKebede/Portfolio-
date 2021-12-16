from .constant import *


def calculate(score, question_length):
    try:

        total = score * (MAX_SCORE / question_length)
        if 100 >= total >= 85:
            return EXCELLENT
        elif 85 > total >= 70:
            return KEEP_IT_UP
        elif 70 > total >= 75:
            return VERY_GOOD
        elif 75 > total >= 60:
            return GOOD
        else:
            return BAD_SCORE
    except ZeroDivisionError:
        return BAD_SCORE


'''      cast a give time difference between previous
          and now called delta_time in to minute and second '''


def change_to_minute_second(seconds):
    minute = int(seconds / 60)
    second = seconds % 60
    return minute, second
