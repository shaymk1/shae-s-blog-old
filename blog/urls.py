from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path("", views.index, name="home"),
    path('<slug:post>/', views.detailed_post, name='post'),
    path("posts/", views.posts, name="posts"),
    # path("post/", views.post, name="post"),
    
 
]
