from django.contrib import admin

from .models import Question, GroupQuestion

admin.site.register(Question)
admin.site.register(GroupQuestion)
