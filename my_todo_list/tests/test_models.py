from django.test import TestCase

from my_todo_list.models import Tag


class TagTest(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test")

    def test_tag_str(self) -> None:
        self.assertEqual(str(self.tag.name), "test")
