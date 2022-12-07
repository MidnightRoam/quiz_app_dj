from django.urls import path, include

from .views import HomePage, QuestionsView, LoginView, LogoutView, SignupView, ResultView, AddQuestionView, \
    AddQuestionGroupView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('questions/<slug:slug>/', QuestionsView.as_view(), name='questions'),
    # path('questions/', QuestionsList.as_view(), name='question-list'),
    path('add_question/', AddQuestionView.as_view(), name='add-question'),
    path('add_group/', AddQuestionGroupView.as_view(), name='add-group'),
    path('signin/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('result/', ResultView.as_view(), name='result')
]
