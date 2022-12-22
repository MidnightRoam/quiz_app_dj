from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.urls import reverse_lazy

from .models import Question, GroupQuestion, Answer, Result
from .forms import AddQuestionForm, AddQuestionGroupForm, AddAnswerForm, ResultForm, QuestionForm


class HomePageView(View):
    """Displayed groups of questions on the home page"""
    template_name = 'pages/index.html'
    paginate_by = 1

    def get(self, request):
        context = {
            'groups': GroupQuestion.objects
                                   .annotate(questions_count=Count('question__id'))
                                   .filter(questions_count__gte=1),  # display group if group have atleast 1 question
            'total_groups': GroupQuestion.objects
                                         .annotate(questions_count=Count('question__id'))
                                         .filter(questions_count__gte=1)
                                         .count(),
            'latest_added_groups': GroupQuestion.objects
                                   .annotate(questions_count=Count('question__id'))
                                   .filter(questions_count__gte=1).order_by("-id")[:7]
        }

        return render(request, 'pages/index.html', context)


class GroupDetailView(DetailView):
    """Group details page view"""
    model = GroupQuestion
    template_name = 'pages/group_page.html'
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(group=self.object)
        return context


class QuestionDetailView(LoginRequiredMixin, DetailView):
    """List of group questions"""
    login_url = 'users:login'
    model = Question
    template_name = 'pages/question_page.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(question=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # get the selected answer from the form submission
        selected_answer = request.POST.get('answer')

        # get the correct answer for the question
        correct_answers = Answer.objects.filter(question=self.object, correct=True)

        # check if the selected answer is correct
        for correct_answer in correct_answers:  # Validation that there can be multiple answers
            if selected_answer == correct_answer.pk:
                # the answer is correct, so update the user's score
                result = Result.objects.get(user=request.user, group=self.object.group)
                result.correct += 1
                result.save()
        # redirect to the next question in the quiz
        next_question = Question.objects.filter(group=self.object.group, pk__gt=self.object.pk).first()
        if next_question:
            return redirect(reverse_lazy('questions', kwargs={'pk': next_question.pk}))
        else:
            # there are no more questions, so redirect to the quiz results page
            return redirect(reverse_lazy('result', kwargs={'pk': self.object.group.pk}))


class QuestionCreateView(CreateView):
    """
    Makes it possible to create questions in test rooms for the administration
    through the site interface, not the admin panel.
    """
    template_name = 'pages/add_question.html'
    form_class = AddQuestionForm
    success_url = reverse_lazy('add-question')


class QuestionGroupCreateView(CreateView):
    """
    Makes it possible to create test rooms for the administration
    through the site interface, not the admin panel.
    After creating a room, it redirects to the page for creating questions.
    """
    template_name = 'pages/add_question_group.html'
    form_class = AddQuestionGroupForm
    success_url = reverse_lazy('add-question')


class AnswerCreateView(CreateView):
    """
    Makes it possible to create a answers for the questions for the administration
    through the site interface, not the admin panel.
    After creating a answer, it redirects to the for creating answers.
    """
    template_name = 'pages/add_answer.html'
    form_class = AddAnswerForm
    success_url = reverse_lazy('add-answer')


class ResultView(DetailView):
    """Quiz result page view"""
    model = GroupQuestion
    template_name = 'pages/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the user's score for the quiz
        result = Result.objects.filter(user=self.request.user, group=self.object)
        if result.exists():
            context['score'] = result.correct
            # get the list of questions the user answered correctly
            correct_answers = Answer.objects.filter(question__group=self.object, correct=True)
            context['correct_answers'] = correct_answers.filter(result__correct=correct_answers)
            # get the list of questions the user answered incorrectly
            incorrect_answers = Answer.objects.filter(question__group=self.object, correct=False)
            context['incorrect_answers'] = incorrect_answers.exclude(result__correct=incorrect_answers)
        else:
            # Display a message to the user
            redirect('index')
        return context
