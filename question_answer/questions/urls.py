from django.urls import path, include

from .views import HomePage, QuestionsView, AddQuestionView, AddQuestionGroupView, AddAnswerView, ResultView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('questions/<int:pk>/', QuestionsView.as_view(), name='questions'),
    path('result/', ResultView.as_view(), name='result'),
    path('add_question/', AddQuestionView.as_view(), name='add-question'),
    path('add_group/', AddQuestionGroupView.as_view(), name='add-group'),
    path('add_answer/', AddAnswerView.as_view(), name='add-answer'),
]
