# Generated by Django 3.2 on 2022-12-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_alter_groupquestion_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupquestion',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
