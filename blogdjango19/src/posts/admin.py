from django.contrib import admin

# Register your models here.
from .models import Post # or from posts.models import Post 


admin.site.register(Post)