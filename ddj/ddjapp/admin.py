from django.contrib import admin
from .models import Room, Request, Chatting, Comment, Recomment


# Register your models here.
admin.site.register(Room)
admin.site.register(Request)
admin.site.register(Chatting)
admin.site.register(Comment)
admin.site.register(Recomment)