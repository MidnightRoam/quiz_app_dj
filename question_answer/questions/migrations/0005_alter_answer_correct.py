# Generated by Django 3.2 on 2022-12-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_groupquestion_number_of_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]
