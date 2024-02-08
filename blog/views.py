from django.shortcuts import render
from .models import Post , TrendingArticles
# 


def index(request):
    model = Post
    posts = Post.objects.all().order_by("-created_at")
    context = {
            "posts": posts, 
             "model": model
             }
    return render(request, "blog/index.html", context)


def post(request):
    return render(request, "blog/post.html")


def posts(request):
    return render(request, "blog/posts.html")


def trending_posts(request):
    model = TrendingArticles
    trending_articles = TrendingArticles.objects.all()
    featured = TrendingArticles.articlemanager.filter(featured=True)[0:3]
    context = {
            "trending_articles": trending_articles, 
            "model": model,
            "featured": featured
             }
    return render(request, "blog/index.html", context)
