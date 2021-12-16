
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('questionanswering.topic.urls')),
    path('questions/', include('questionanswering.questionanswer.urls'))
]
