# Generated by Django 3.2 on 2022-12-08 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupquestion',
            name='slug',
        ),
    ]
