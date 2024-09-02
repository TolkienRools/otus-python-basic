from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_at = models.DateField()


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False)

    tasks = models.ManyToManyField(
        Task,
        through="TaskTag",
        through_fields=("tag", "task"),
        related_name="tags"
    )


class TaskTag(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)