from django.db import models


class GroupQuestion(models.Model):
    group_name = models.CharField(max_length=250)
    description = models.CharField(max_length=100, blank=True, default='')
    number_of_questions = models.IntegerField(default=1)

    def __str__(self):
        return self.group_name


class Question(models.Model):
    text = models.CharField(max_length=250, null=True)
    group = models.ForeignKey(GroupQuestion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.text} ({self.group})"


class Answer(models.Model):
    text = models.CharField(max_length=250, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupQuestion, on_delete=models.CASCADE, null=True)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({self.question})"
