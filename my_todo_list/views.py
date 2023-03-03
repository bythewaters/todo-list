from django.views import generic
from django.shortcuts import render

from my_todo_list.models import Tag


def index(request):
    return render(request, "my_todo_list/task.html")


class TagListView(generic.ListView):
    model = Tag
    template_name = "my_todo_list/tag.html"
