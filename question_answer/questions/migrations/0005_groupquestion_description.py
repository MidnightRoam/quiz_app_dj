# Generated by Django 3.2 on 2022-12-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_groupquestion_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupquestion',
            name='description',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]