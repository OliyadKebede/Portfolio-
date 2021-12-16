from django.urls import path
from . import views

app_name = 'QA'

urlpatterns =[
    path('<int:topic_id>/', views.questions_page, name='question_page'),
    path('new/<int:topic_id>/' , views.new_question , name='new_question'),
    path('result/<int:topic_id>/' , views.results, name='results')
]
