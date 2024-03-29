# Generated by Django 4.1.7 on 2023-03-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_todo_list", "0003_alter_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(default=2, max_length=63),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                db_constraint=False,
                null=True,
                related_name="task",
                to="my_todo_list.tag",
            ),
        ),
    ]
