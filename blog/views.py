from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    model = Post
    posts = Post.objects.all().order_by("-created_at")
    context = {"posts": posts, "model": model}
    return render(request, "blog/index.html", context)


def post(request):
    return render(request, "blog/post.html")


def posts(request):
    return render(request, "blog/posts.html")
