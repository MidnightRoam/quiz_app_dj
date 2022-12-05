from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Question


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
