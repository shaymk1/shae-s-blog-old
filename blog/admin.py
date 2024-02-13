from django.contrib import admin
from .models import Post, TrendingArticles, DetailedPost

# Register your models here.
admin.site.register(Post)
admin.site.register(TrendingArticles)
admin.site.register(DetailedPost)
