# Generated by Django 3.2 on 2022-12-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20221209_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupquestion',
            name='number_of_questions',
            field=models.IntegerField(default=1),
        ),
    ]
