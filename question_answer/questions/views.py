from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Question, GroupQuestion
from .forms import AddQuestionForm


class HomePage(View):
    template_name = 'index.html'
    # context_object_name = 'questions'

    def get(self, request):
        return render(request, 'index.html', {
            'groups': GroupQuestion.objects.all(),
            'total_groups': GroupQuestion.objects.all().count()
                                              })

    def post(self, request):
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for question in questions:
            total += 1
            if questions.answer == request.POST.get(question.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        context = {
            'score': score,
            'wrong': wrong,
            'time': request.POST.get('timer'),
            'correct': correct,
            'total': total,
            'percent': percent
        }
        return render(request, 'index.html', context)


class QuestionsView(ListView):
    model = GroupQuestion
    template_name = 'question_page.html'
    # slug_url_kwarg = 'slug'
    context_object_name = 'questions'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['questions'] = Question.objects.filter(group__slug=slug)
        return context


# class QuestionsList(ListView):
#     model = Question
#     template_name = 'question_page.html'
#     context_object_name = 'question_list'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['questions'] = Question.objects.all()
#         return context

# class AddQuestion(View):
#
#     def post(self, request):
#         if request.user.is_staff:
#             form = AddQuestionForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')
#             context = {'form': form}
#             return render(request, 'add_question.html', context)
#         else:
#             return redirect('index')


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
        if user is not None:
            login(request, user)
            return redirect('/')
        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
