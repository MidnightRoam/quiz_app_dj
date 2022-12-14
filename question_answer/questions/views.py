from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Question, GroupQuestion, Answer, Result
from .forms import AddQuestionForm, AddQuestionGroupForm, AddAnswerForm, ResultForm


class HomePage(View):
    """Displayed groups of questions on the home page"""
    template_name = 'index.html'

    def get(self, request):
        context = {
            'groups': GroupQuestion.objects
                                   .annotate(questions_count=Count('question__id'))
                                   .filter(questions_count__gte=1),  # display group if group have atleast 1 question
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
        form = ResultForm()
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
            # 'percent': percent,
            'results': form,
        }
        if qnumber == questions.count():
            return render(request, 'result.html', context)
        else:
            qnumber += 1
            return redirect(f'/questions/{pk}/?page={qnumber}')

    # def get_queryset(self, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     questions = Question.objects.filter(group__pk=pk)
    #     answers = Answer.objects.filter(question__pk=pk)
    #     return Question.objects.filter(group__pk=pk)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        p = Paginator(Question.objects
                              .select_related()
                              .filter(group__pk=pk), self.paginate_by)  # pagination of question answers
        context['questions'] = p.page(context['page_obj'].number)
        # context['questions'] = Question.objects.filter(group__pk=pk)
        context['answers'] = Answer.objects.filter(question__pk=pk)
        return context


class AddQuestionView(CreateView):
    """
    Makes it possible to create questions in test rooms for the administration
    through the site interface, not the admin panel.
    """
    template_name = 'add_question.html'
    model = Question
    fields = '__all__'
    success_url = '/add_question/'


class AddQuestionGroupView(CreateView):
    """
    Makes it possible to create test rooms for the administration
    through the site interface, not the admin panel.
    After creating a room, it redirects to the page for creating questions.
    """
    template_name = 'add_question_group.html'
    model = GroupQuestion
    fields = '__all__'
    success_url = '/add_question/'


class AddAnswerView(CreateView):
    """
    Makes it possible to create a answers for the questions for the administration
    through the site interface, not the admin panel.
    After creating a answer, it redirects to the for creating answers.
    """
    template_name = 'add_answer.html'
    model = Answer
    fields = '__all__'
    success_url = '/add_answer/'


class ResultView(ListView):
    template_name = 'result.html'
    model = Result

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_questions'] = Result.objects.filter().count()
        return context
