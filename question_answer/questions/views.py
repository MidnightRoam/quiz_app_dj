from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.urls import reverse_lazy

from .models import Question, GroupQuestion, Answer, Result
from .forms import AddQuestionForm, AddQuestionGroupForm, AddAnswerForm, ResultForm, QuizForm


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
                                         .count(),
            'latest_added_groups': GroupQuestion.objects
                                   .annotate(questions_count=Count('question__id'))
                                   .filter(questions_count__gte=1).order_by("-id")[:7]
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
        question_form = QuizForm(request.POST)
        answer_form = AddAnswerForm(request.POST)
        result_form = ResultForm()

        if question_form.is_valid() and answer_form.is_valid():
            # Save the question to the database
            question = question_form.save()
            # Save the answer to the database
            answer = answer_form.save()

            result = result_form.save(commit=False)
            result.question = question
            result.answer = answer
            result.save()

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
        }
        if 'page' in request.GET:
            # get the current value of the page parameter from the request
            page = request.GET.get('page')
        else:
            # initialize the page parameter to 0 if it is not present in the request
            page = 1

        if qnumber == questions.count():
            return render(request, 'result.html', context)
        else:
            qnumber += 1
            page = qnumber
            # page = str(page)
            return redirect(f'/questions/{pk}/?page={qnumber}')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Question.objects
                              .select_related()
                              .filter(group__pk=self.kwargs['pk']), self.paginate_by)  # pagination of question answers
        context['questions'] = p.page(context['page_obj'].number)
        # context['questions'] = Question.objects.filter(group__pk=pk)
        context['answers'] = Answer.objects.filter(question__pk=self.kwargs['pk'])
        return context


class AddQuestionView(CreateView):
    """
    Makes it possible to create questions in test rooms for the administration
    through the site interface, not the admin panel.
    """
    template_name = 'add_question.html'
    form_class = AddQuestionForm
    success_url = reverse_lazy('add_question')


class AddQuestionGroupView(CreateView):
    """
    Makes it possible to create test rooms for the administration
    through the site interface, not the admin panel.
    After creating a room, it redirects to the page for creating questions.
    """
    template_name = 'add_question_group.html'
    form_class = AddQuestionGroupForm
    success_url = reverse_lazy('add-question')


class AddAnswerView(CreateView):
    """
    Makes it possible to create a answers for the questions for the administration
    through the site interface, not the admin panel.
    After creating a answer, it redirects to the for creating answers.
    """
    template_name = 'add_answer.html'
    form_class = AddAnswerForm
    success_url = reverse_lazy('add_answer')


class ResultView(ListView):
    template_name = 'result.html'
    model = Result

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_questions'] = Result.objects.filter().count()
        return context
