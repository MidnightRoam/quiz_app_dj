# Generated by Django 3.2 on 2022-12-09 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_answer_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.groupquestion'),
        ),
    ]