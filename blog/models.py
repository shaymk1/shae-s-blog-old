from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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
    sub_title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    time_required_to_read = models.CharField(
        max_length=250, 
        default="2 minutes"
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
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
