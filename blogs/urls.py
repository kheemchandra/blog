from django.urls import path 

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]