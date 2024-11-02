from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Groups(models.Model):
    name = models.TextField(null=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "+"),
        ("in_progress", "="),
        ("done", "-"),
        ("expired","!"),]
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank= True)
    due_time = models.DateTimeField(verbose_name="due_time", null=True, blank= True)
    status = models.CharField(max_length=27, choices=STATUS_CHOICES, default="todo")
    priority = models.IntegerField(default="5")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task")
    group = models.ForeignKey(to=Groups, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Comments(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField()