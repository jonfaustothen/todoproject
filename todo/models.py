from unicodedata import name
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    completed = models.BooleanField(default=False)

class Comment(models.Model):
    body = models.TextField()
    #ForeignKey: coonects the Comment model to the TEst model
    # on_delete-models.CASCADE: if the task gets deleted, we want that to "cascade" and delete all of the comments for that task
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Note(models.Model):
    # Only one thing in this model: a text column.
    text = models.TextField()