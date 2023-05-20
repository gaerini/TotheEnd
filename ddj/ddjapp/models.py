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
    
    request_member = models.IntegerField(null=True)
    matched = models.BooleanField(null=False)

    def __str__(self):
        return self.give_food

class Request(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room2')
    reciever = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='Request')
    req_member = models.IntegerField()

    def __str__(self):
        return self.sender
    

class Article(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    category=models.CharField(max_length=50, null=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()

    def __str__(self):
        return self.content
    
class Recomment(models.Model):
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomments')
    content=models.TextField()

    def __str__(self):
        return self.content