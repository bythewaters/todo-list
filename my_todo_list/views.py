from django.urls import reverse_lazy
from django.views import generic

from my_todo_list.models import Tag, Task


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
    model = Task
    template_name = "my_todo_list/tag_delete_form.html"


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "my_todo_list/task.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "my_todo_list/tag_update_create_form.html"
    success_url = reverse_lazy("my_todo_list:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "my_todo_list/tag_update_create_form.html"
    success_url = reverse_lazy("my_todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "my_todo_list/task_delete_form.html"
