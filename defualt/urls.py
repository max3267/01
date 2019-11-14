from django.urls import path
from .poll import *

urlpatterns = [
    path('', PollList.as_view()),
    path('<int:pk>/', PollDetail.as_view(), name='poll_view'),
    path('vote/<int:oid>/',Pollvote.as_view()),
    path('create/',PollCreateas_view()),
    path('<int:pk>/update/',PollCreateas_view()),
    path('<int:pid>/create/'OptionCreate.as_view()),


]