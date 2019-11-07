from django.urls import path
from . import views

urlpatterns = [
    path('poll/', views.PollList.as_view()),
    path('poll/<int:pk>/', views.PollDetail.as_view()),
    path('poll/vote/<int:oid>/',views.Pollvote.as_view()),
]