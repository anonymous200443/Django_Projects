# Generated by Django 5.0.6 on 2025-01-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_task_description_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(default=3, max_length=120),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default=3, max_length=200),
        ),
    ]