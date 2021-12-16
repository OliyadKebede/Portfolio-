from django.contrib import admin
from ..topic.models import Topic
# Register your models here.
from ..questionanswer.models import  Question ,Choice ,Score
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Score)