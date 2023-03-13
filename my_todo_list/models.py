from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    mark = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="task")

    class Meta:
        ordering = ["mark", "-date_time"]
