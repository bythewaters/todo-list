# Generated by Django 4.1.7 on 2023-03-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_todo_list", "0005_alter_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(related_name="task", to="my_todo_list.tag"),
        ),
    ]
