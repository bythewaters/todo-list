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


class TagViewTest(TestCase):
    def setUp(self) -> None:
        self.tag1 = Tag.objects.create(name="test_tag1")
        self.tag2 = Tag.objects.create(name="test_tag2")
        self.tags_queryset = Tag.objects.all()

    def test_tag_list(self):
        url = reverse("todo_list:tag-list")
        response = self.client.get(url)
        self.assertEqual(
            list(response.context["tag_list"]),
            list(self.tags_queryset)
        )
        self.assertTemplateUsed(response, "my_todo_list/tag.html")

    def test_tag_create(self):
        url = reverse("todo_list:tag-create")
        response = self.client.post(url, {"name": "test_tag3"})
        self.assertTrue(Tag.objects.filter(name="test_tag3").exists())
        self.assertRedirects(response, "/tags/")

    def test_tag_update(self):
        response = self.client.post(reverse(
            "my_todo_list:tag-update",
            args=[self.tag1.id]),
            {"name": "updated_tag"}
        )
        self.tag1.refresh_from_db()
        self.assertEqual(self.tag1.name, "updated_tag")
        self.assertRedirects(response, "/tags/")

    def test_tag_delete(self):
        response = self.client.post(reverse(
            "my_todo_list:tag-delete",
            args=[self.tag1.id]
        ))
        self.assertFalse(Tag.objects.filter(name="test_tag1").exists())
        self.assertRedirects(response, "/tags/")


class TaskViewTest(TestCase):
    def setUp(self) -> None:
        self.task1 = Task.objects.create(
            content="test_cont1",
        )
        self.task2 = Task.objects.create(
            content="test_cont2",
        )
        tag1 = Tag.objects.create(name="test_tag1")
        tag2 = Tag.objects.create(name="test_tag2")
        self.task1.tags.add(tag1)
        self.task2.tags.add(tag2)
        self.task_queryset = Task.objects.all()

    def test_task_list(self):
        url = reverse("todo_list:task-list")
        response = self.client.get(url)
        self.assertEqual(
            list(response.context["task_list"]),
            list(self.task_queryset)
        )
        self.assertTemplateUsed(response, "my_todo_list/task.html")

    def test_task_create(self):
        url = reverse("todo_list:task-create")
        response = self.client.post(url, {"content": "test_task3"})
        self.assertTrue(Task.objects.filter(content="test_task3").exists())
        self.assertRedirects(response, "/")

    def test_task_update_tag(self):
        tag = Tag.objects.create(name="test")
        response = self.client.post(reverse(
            "my_todo_list:task-update-tag",
            args=[self.task1.id]),
            {"tags": tag.id}
        )
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.tags.filter(name="test").exists())
        self.assertRedirects(response, "/")

    def test_task_delete(self):
        response = self.client.post(reverse(
            "my_todo_list:task-delete",
            args=[self.task1.id]
        ))
        self.assertFalse(Task.objects.filter(content="test_task1").exists())
        self.assertRedirects(response, "/")
