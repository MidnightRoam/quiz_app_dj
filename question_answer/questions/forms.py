from django.forms import ModelForm

from .models import Question, GroupQuestion, Answer


class QuizForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AddQuestionGroupForm(ModelForm):
    class Meta:
        model = GroupQuestion
        fields = "__all__"


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AddAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
