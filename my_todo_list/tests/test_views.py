from django.test import TestCase
from django.urls import reverse

from my_todo_list.models import Task, Tag


class UpdateMarkTest(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(
            content="TestContent",
            deadline="2023-10-10T10:12",
            mark=False
        )
        self.tag = Tag.objects.create(
            name="TestTag"
        )
        self.task.tags.add(self.tag)

    def test_change_mark_task(self):
        self.client.post(
            reverse("my_todo_list:task-update-mark", args=[self.task.id]),
        )
        self.task.refresh_from_db()
        self.assertEqual(self.task.mark, True)
