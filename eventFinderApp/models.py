from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=0)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    host = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'hosting_events', default=0)
    venue = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category', related_name='event')
    attendees = models.ManyToManyField(User, related_name = 'attending_events')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name