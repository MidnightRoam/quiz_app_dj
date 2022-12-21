from django.forms import ModelForm

from .models import Question, GroupQuestion, Answer, Result


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class ResultForm(ModelForm):
    class Meta:
        model = Result
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
