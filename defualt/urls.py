from django.urls import path
from .views import *


urlpatterns = [
    path('', PollList.as_view()),
    path('<int:pk>/', PollDetail.as_view(), name='poll_view'),
    path('vote/<int:oid>/',Pollvote.as_view()),
    path('create/',PollCreate.as_view()),
    path('<int:pk>/update/',PollUpdate.as_view()),
    path('<int:pid>/create/',OptionCreate.as_view(), name='option_create'),


]