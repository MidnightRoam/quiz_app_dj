from django.urls import reverse

from django.contrib.auth.models import User
from django.db import models


class GroupQuestion(models.Model):
    group_name = models.CharField(max_length=250)
    description = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse('questions', kwargs={'pk': self.pk})


class Question(models.Model):
    text = models.CharField(max_length=250, null=True)
    group = models.ForeignKey(GroupQuestion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.text} ({self.group})"


class Answer(models.Model):
    text = models.CharField(max_length=250, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupQuestion, on_delete=models.CASCADE, null=True)
    correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return f"{self.text} ({self.group})"


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupQuestion, on_delete=models.CASCADE, default='')
    correct = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
