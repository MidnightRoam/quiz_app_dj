from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question, GroupQuestion
from .forms import AddQuestionForm, AddQuestionGroupForm


class HomePage(View):
    template_name = 'index.html'
    # context_object_name = 'questions'

    def get(self, request):
        return render(request, 'index.html', {
            'groups': GroupQuestion.objects.all(),
            'total_groups': GroupQuestion.objects.all().count()
          })

    # def post(self, request):
    #     questions = Question.objects.all()
    #     score = 0
    #     wrong = 0
    #     correct = 0
    #     total = 0
    #     for question in questions:
    #         total += 1
    #         if questions.answer == request.POST.get(question.question):
    #             score += 10
    #             correct += 1
    #         else:
    #             wrong += 1
    #     percent = score / (total * 10) * 100
    #     context = {
    #         'score': score,
    #         'wrong': wrong,
    #         'time': request.POST.get('timer'),
    #         'correct': correct,
    #         'total': total,
    #         'percent': percent
    #     }
    #     return render(request, 'result.html', context)


class QuestionsView(LoginRequiredMixin, ListView):
    model = GroupQuestion
    template_name = 'question_page.html'
    context_object_name = 'questions'
    login_url = '/signin/'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs['slug']
        return Question.objects.filter(group__slug=slug)


class AddQuestionView(View):
    template_name = 'add_question.html'

    def get(self, request):
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
            return redirect('/')
        context = {'form': form}
        return render(request, 'add_question_group.html', context)


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
        return render(request, 'login.html')


class SignupView(View):

    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2 and username:
                user = User.objects.create_user(username=username, password=password1)
                login(request, user)
                return redirect('/')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class ResultView(TemplateView):
    template_name = 'result.html'
