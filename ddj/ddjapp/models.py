from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room')
    current_member = models.TextField()
    want_member = models.IntegerField()
    matched = models.BooleanField(null=False)
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
        return self.sender
    

class Article(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    category=models.CharField(max_length=50, null=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return self.content
=======
        return self.title
>>>>>>> c6c1c5fc17143a51f940901392a96ece1909a152
    
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