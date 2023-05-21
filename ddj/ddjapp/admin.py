from django.contrib import admin
from .models import Room, Article, Comment, Request


# Register your models here.
admin.site.register(Room)
admin.site.register(Request)
admin.site.register(Article)
admin.site.register(Comment)