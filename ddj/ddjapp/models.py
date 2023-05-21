from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room')
    current_member = models.TextField()
    want_member = models.IntegerField()
    matched = models.IntegerField(default=0)
    talk_topic = models.CharField(max_length=20)
    age = models.TextField()
    give_food = models.TextField()
    sex = models.CharField(max_length=50)
   
    def __str__(self):
        return str(self.id)

class Request(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='recieved')
    member = models.TextField()
    talk_topic = models.CharField(max_length=20)
    age = models.TextField()
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.talk_topic
    

class Chatting(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, name='roomLeader')
    request = models.ForeignKey(Request, on_delete=models.CASCADE, name='requester')
    content = models.TextField()

    def __str__(self):
        return self.content
    
class Comment(models.Model):
    article=models.ForeignKey(Chatting, on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()

    def __str__(self):
        return self.content
    
class Recomment(models.Model):
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomments')
    content=models.TextField()

    def __str__(self):
        return self.content