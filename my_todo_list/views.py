from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from my_todo_list.forms import TaskForm, UpdateTaskTagForm
from my_todo_list.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "my_todo_list/tag.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    template_name = "my_todo_list/tag_update_form.html"
    success_url = reverse_lazy("my_todo_list:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)
    template_name = "my_todo_list/tag.html"
    success_url = reverse_lazy("my_todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "my_todo_list/tag.html"
    success_url = reverse_lazy("my_todo_list:tag-list")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "my_todo_list/task.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "my_todo_list/tag_update_form.html"
    success_url = reverse_lazy("my_todo_list:task-list")


def update_mark(request, pk):
    tasks = Task.objects.all().filter(id=pk)
    for task in tasks:
        if task.mark is False:
            task.mark = True
            task.save()
        else:
            task.mark = False
            task.save()
    return redirect("my_todo_list:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "my_todo_list/task_update_form.html"
    success_url = reverse_lazy("my_todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "my_todo_list/task.html"
    success_url = reverse_lazy("my_todo_list:task-list")


class UpdateTagView(generic.UpdateView):
    model = Task
    form_class = UpdateTaskTagForm
    template_name = "my_todo_list/update_task_tag.html"
    success_url = reverse_lazy("my_todo_list:task-list")
