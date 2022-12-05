from django.db import models


class GroupQuestion(models.Model):
    group_name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.group_name


class Question(models.Model):
    question = models.CharField(max_length=250, null=True)
    group = models.ForeignKey(GroupQuestion, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=250, null=True)
    option1 = models.CharField(max_length=250, null=True)
    option2 = models.CharField(max_length=250, null=True)
    option3 = models.CharField(max_length=250, null=True)
    option4 = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.question
