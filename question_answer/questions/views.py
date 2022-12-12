from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Question, GroupQuestion, Answer
from .forms import AddQuestionForm, AddQuestionGroupForm, AddAnswerForm


class HomePage(View):
    """Displayed groups of questions on the home page"""
    template_name = 'index.html'

    def get(self, request):
        context = {
            'groups': GroupQuestion.objects
                                   .annotate(questions_count=Count('question__id'))
                                   .filter(questions_count__gte=1),  # display group if group have 1+ question
            'total_groups': GroupQuestion.objects
                                         .annotate(questions_count=Count('question__id'))
                                         .filter(questions_count__gte=1)
                                         .count()
        }

        return render(request, 'index.html', context)


class QuestionsView(LoginRequiredMixin, ListView):
    """List of group questions"""
    model = Question
    template_name = 'question_page.html'
    context_object_name = 'questions'
    login_url = 'users:login'
    paginate_by = 1

    def post(self, request, pk):
        questions = Question.objects.filter(group__pk=pk)
        answers = Answer.objects.filter(question__pk=pk)

        score = 0
        wrong = 0
        correct = 0
        total = 0
        qnumber = 1
        for question in answers:
            total += 1
            if request.POST.get(question.correct) is True:
                score += 10
                correct += 1
            else:
                wrong += 1
        # percent = score / (total * 10) * 100
        context = {
            'score': score,
            'wrong': wrong,
            'correct': correct,
            'total': total,
            # 'percent': percent
        }

        if qnumber == questions.count():
            return render(request, 'result.html', context)
        else:
            return redirect(f'/questions/{pk}/?page={qnumber}')

    # def get_queryset(self, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     questions = Question.objects.filter(group__pk=pk)
    #     answers = Answer.objects.filter(question__pk=pk)
    #     return Question.objects.filter(group__pk=pk)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        p = Paginator(Question.objects.select_related().filter(group__pk=pk), self.paginate_by)  # pagination of question answers
        context['questions'] = p.page(context['page_obj'].number)
        # context['questions'] = Question.objects.filter(group__pk=pk)
        context['answers'] = Answer.objects.filter(question__pk=pk)
        return context


class AddQuestionView(View):
    """
    Makes it possible to create questions in test rooms for the administration
    through the site interface, not the admin panel.
    """

    template_name = 'add_question.html'

    def get(self, request, **kwargs):
        if request.user.is_staff:
            form = AddQuestionForm()
            return render(request, 'add_question.html')
        else:
            return redirect('index')

    def post(self, request):
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form': form}
        return render(request, 'add_question.html', context)


class AddQuestionGroupView(View):
    """
    Makes it possible to create test rooms for the administration
    through the site interface, not the admin panel.
    After creating a room, it redirects to the page for creating questions.
    """

    template_name = 'add_question_group.html'

    def get(self, request):
        if request.user.is_staff:
            form = AddQuestionGroupForm()
            return render(request, 'add_question_group.html')
        else:
            return redirect('index')

    def post(self, request):
        form = AddQuestionGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-question')
        context = {'form': form}
        return render(request, 'add_question_group.html', context)


class AddAnswerView(View):
    """
    Makes it possible to create a answers for the questions for the administration
    through the site interface, not the admin panel.
    After creating a answer, it redirects to the page of question.
    """

    template_name = 'add_answer.html'

    def get(self, request):
        if request.user.is_staff:
            form = AddAnswerForm()
            return render(request, 'add_answer.html')
        else:
            return redirect('index')

    def post(self, request):
        form = AddAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form': form}
        return render(request, 'add_answer.html', context)


class ResultView(TemplateView):
    template_name = 'result.html'
