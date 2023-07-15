from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
 

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_photo = models.ImageField(upload_to = 'blogs')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='blog')
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    title = models.CharField(max_length= 30)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    title = models.CharField(max_length= 30)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    time = models.DateTimeField(auto_now_add = True)
    comment = models.TextField()
    email = models.EmailField()
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering= ('time',)
    
    def __str__(self):
        return self.email