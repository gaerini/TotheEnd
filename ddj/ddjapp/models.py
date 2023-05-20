from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room')
    title = models.CharField(max_length=20)
    current_member = models.TextField()
    want_member = models.TextField()
    finished = models.BooleanField()
    # template = models.ForeignKey(Template, related_name = 'room')

    def __str__(self):
        return self.title
    
class Template(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='template')
    talk_topic = models.CharField(max_length=20)
    age = models.TextField()
    give_food = models.TextField()

    def __str__(self):
        return self.room.title

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
