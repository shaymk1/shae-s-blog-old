# from email.policy import default
# from pyexpat import model
# from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    image = models.ImageField(
        null=True, blank=True, 
        upload_to="article",
        default="placeholder.png"
        )
    category = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    time_required_to_read = models.CharField(
        max_length=250, 
        default="2 Min Read"
        )
    title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250, unique=True)
    intro = models.TextField(blank=True)
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )

    class Meta:
        ordering = ("-created_at",)  # decending order

    def __str__(self):
        return self.title
    

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() .filter(status='published') 
       

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class DetailedPost(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')

    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(
             null=True, blank=True, 
             upload_to="article",
             default="placeholder.png")
    # body = RichTextUploadingField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    
    status = models.CharField(max_length=10, choices=options, default='draft')

    objects = models.Manager()  # default manager
    # articlemanager = ArticleManager()  # custom manager

    def get_absolute_url(self):
        return reverse('blog:article', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.headline


class TrendingArticles(models.Model):
    image = models.ImageField(
            null=True, blank=True, 
            upload_to="article",
            default="placeholder.png"
           )
    article_number = models.CharField(max_length=250)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    time_required_to_read = models.CharField(
        max_length=250, 
        default="2 Min Read"
        )
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
