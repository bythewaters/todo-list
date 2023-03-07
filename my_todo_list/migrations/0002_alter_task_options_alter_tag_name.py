# Generated by Django 4.1.7 on 2023-03-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_todo_list", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["mark", "date_time"]},
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]