from django.urls import path
from .poll import *

urlpatterns = [
    path('', PollList.as_view()),
    path('<int:pk>/', PollDetail.as_view()),
    path('vote/<int:oid>/',Pollvote.as_view()),
]