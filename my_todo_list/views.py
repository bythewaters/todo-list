from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from my_todo_list.models import Tag


def index(request):
    return render(request, "my_todo_list/task.html")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "my_todo_list/tag.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "my_todo_list/tag_update_create_form.html"
    success_url = reverse_lazy("my_todo_list:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "my_todo_list/tag_update_create_form.html"
    success_url = reverse_lazy("my_todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "my_todo_list/tag_delete_form.html"
