from .models import User, Category, Post, Comment
from django.contrib import admin

# Register your models here.
admin.site.site_header = "Blog API Admin"
admin.site.site_title = "Blog API Admin Portal"
admin.site.index_title = "Welcome to the Blog API Admin Portal"

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
