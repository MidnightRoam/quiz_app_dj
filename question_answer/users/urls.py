from django.urls import path, include

from .views import LoginView, LogoutView, SignupView

app_name = "users"

urlpatterns = [
    path('signin/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
