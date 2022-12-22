from django.urls import path, include

from .views import HomePageView, QuestionDetailView, QuestionCreateView, QuestionGroupCreateView, AnswerCreateView, ResultView, GroupDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('<int:pk>/question/', QuestionDetailView.as_view(), name='questions'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group'),
    path('<int:pk>/results/', ResultView.as_view(), name='result'),
    path('add_question/', QuestionCreateView.as_view(), name='add-question'),
    path('add_group/', QuestionGroupCreateView.as_view(), name='add-group'),
    path('add_answer/', AnswerCreateView.as_view(), name='add-answer'),
]
