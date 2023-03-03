from django.urls import path

from my_todo_list.views import TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskListView, TaskDeleteView, \
    TaskUpdateView

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/delete", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "my_todo_list"
