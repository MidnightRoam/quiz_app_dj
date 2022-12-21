from django.urls import path, include

from .views import HomePage, QuestionsView, AddQuestionView, AddQuestionGroupView, AddAnswerView, ResultView, GroupDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('<int:pk>/question/', QuestionsView.as_view(), name='questions'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group'),
    path('<int:pk>/results/', ResultView.as_view(), name='result'),
    path('add_question/', AddQuestionView.as_view(), name='add-question'),
    path('add_group/', AddQuestionGroupView.as_view(), name='add-group'),
    path('add_answer/', AddAnswerView.as_view(), name='add-answer'),
]
