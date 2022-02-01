from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name= 'blogs'),
    path('<int:id>/', views.blog_detail, name= 'blogs_detail'),
    path('tag/<slug:tag>/', views.blog_tag, name= 'tag'),
    path('category/<slug:category>/', views.blog_category, name= 'category'),
    path('search/', views.search, name= 'search'),
]