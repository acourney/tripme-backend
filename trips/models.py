from django.db import models
from users.models import User

class Trip(models.Model):
    label = models.CharField(max_length=200)
    destination = models.CharField(max_length=500)
    owner = models.ForeignKey('users.User', related_name='trips', on_delete=models.CASCADE, default='1')
    photo = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.label

class Todo(models.Model):
    summary = models.CharField(max_length=200)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="todos")
    body = models.TextField()
    owner = models.ForeignKey('users.User', related_name='todos', on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.summary
