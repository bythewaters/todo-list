from django.contrib import admin
from django.contrib.admin import ModelAdmin

from my_todo_list.models import Task


@admin.register(Task)
class FeedBackAdmin(ModelAdmin):
    list_display = ("content", "date_time", "deadline")
    ordering = ("date_time",)
