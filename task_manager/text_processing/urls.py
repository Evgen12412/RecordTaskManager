from django.urls import path, include

from .views import *

urlpatterns = [
    path('transcribe/<int:recording_id>/', Transcribe.as_view(), name='transcribe_audio'),
]