# Generated by Django 4.1.7 on 2023-03-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_todo_list", "0006_alter_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(default=None),
        ),
    ]
