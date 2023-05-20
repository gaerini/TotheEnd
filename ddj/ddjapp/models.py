from django.contrib.auth.models import User
from django.db import models




class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room')
    current_member = models.TextField()
    want_member = models.TextField()
    finished = models.BooleanField()
    talk_topic = models.CharField(max_length=20)
    age = models.TextField()
    give_food = models.TextField()
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.give_food
