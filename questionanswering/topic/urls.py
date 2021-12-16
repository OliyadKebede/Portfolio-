from django.urls import path
from . import views
from .views import TopicCreateViewForm, TopicTimeUpdate ,TopicDetailView
from .views import TopicListView ,TopicResultDetailView
app_name = 'Topic'

urlpatterns = [
    path('', TopicListView.as_view(), name='check_index'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_welcome'),
    path('topic/new/', TopicCreateViewForm.as_view(), name='add_topic'),
    path('topic/<int:pk>/new_time', TopicTimeUpdate.as_view(), name='add_topic_time'),
    path('results/<int:pk>/', TopicResultDetailView.as_view(), name='total_result')

]
