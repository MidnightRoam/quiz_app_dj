from django.contrib import admin

from .models import Question, GroupQuestion, Answer


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionInline(admin.TabularInline):
    model = Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Question section in the admin panel where you can create
    a question by selecting a quiz set and question name,
    and also, immediately create answers to this question
    """
    list_display = ('text', 'group')
    list_filter = ['group']
    inlines = [AnswerInline]


@admin.register(GroupQuestion)
class GroupQuestionAdmin(admin.ModelAdmin):
    """
    Section in the admin panel of the test set with questions
    where you can change, add, question and answers, mark answers as correct
    """

    list_display = ('group_name', 'description')
    list_filter = ['group_name']
    inlines = [QuestionInline, AnswerInline]
