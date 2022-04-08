from django.db import models

class Trip(models.Model):
    label = models.CharField(max_length=200)
    destination = models.CharField(max_length=500)
    # photo = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True)

    def __str__(self):
        return self.label

class Todo(models.Model):
    summary = models.CharField(max_length=200)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="todos")
    body = models.TextField()

    def __str__(self):
        return self.summary

