from django.contrib import admin
from app.models import Blog,Comment
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['user','title','discription']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['blogger','comment']