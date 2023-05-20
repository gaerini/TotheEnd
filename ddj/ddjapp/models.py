from django.contrib.auth.models import User
from django.db import models




class Room(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room')
    title = models.CharField(max_length=20)
    current_member = models.IntegerField()
    want_member = models.TextField()
    finished = models.BooleanField()
    # template = models.ForeignKey(Template, related_name = 'room')

    def __str__(self):
        return self.title
    
class Template(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='template')
    talk_topic = models.CharField(max_length=20)
    hobby = models.CharField(max_length=20)
    age = models.IntegerField()
    give_food = models.BooleanField()

    def __str__(self):
        return self.room.title
