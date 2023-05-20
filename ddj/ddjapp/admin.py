from django.contrib import admin
from .models import Room, Template, Article, Comment


# Register your models here.
admin.site.register(Room)
admin.site.register(Template)
admin.site.register(Article)
admin.site.register(Comment)