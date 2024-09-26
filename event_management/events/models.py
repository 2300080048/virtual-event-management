# accounts/models.py
from django.contrib.auth.models import User

# events/models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Session(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()
