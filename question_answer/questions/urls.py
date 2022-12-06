from django.urls import path, include

from .views import HomePage, QuestionsView, LoginView, LogoutView, SignupView, ResultView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('questions/<slug:slug>/', QuestionsView.as_view(), name='questions'),
    # path('questions/', QuestionsList.as_view(), name='question-list'),
    # path('addQuestion/', AddQuestion, name='addQuestion'),
    path('signin/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    # path('signup/', RegisterPage, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('result/', ResultView.as_view(), name='result')
]
