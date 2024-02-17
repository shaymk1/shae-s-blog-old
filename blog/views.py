from webbrowser import get
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Post, TrendingArticles, Tag, DetailedPost
from django.db.models import Q
# 


def index(request):
    model = Post
    posts = Post.objects.all().order_by("-created_at")
    context = {
            "posts": posts, 
             "model": model
             }
    return render(request, "blog/index.html", context)


# def post(request):
#     return render(request, "blog/post.html")


def posts(request):
     # get query from request
    query = request.GET.get('query')
    # print(query)
    # Set query to '' if None
    if query is None:
        query = ''

    # articles = Article.articlemanager.all()
    # search for query in headline, sub headline, body
    # articles = Post.articlemanager.filter(
    #     Q(headline__icontains=query) |
    #     Q(sub_headline__icontains=query) |
    #     Q(body__icontains=query)
    # )

    tags = Tag.objects.all()

    context = {
        
        'tags': tags,
    }
    return render(request, "blog/posts.html", context)


def detailed_post(request, post):
    model = DetailedPost
    single_post = get_object_or_404(DetailedPost, slug=post)
    context = {
            " single_post":  single_post, 
             "model": model
             }
    return render(request, "blog/post.html", context)


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
