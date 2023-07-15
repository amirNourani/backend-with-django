from django.shortcuts import render
from .models import Blog, Category, Comment, Tag
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def blogs(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 3) # Show 3 blogs per page.
    
    page_number = request.GET.get('page')
    
    try:
        blog_list = paginator.get_page(page_number)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    context = {
        'blogs': blog_list,
    }
    
    return render(request, 'blogs/blog.html', context)


def blog_detail(request, id):
    blog = Blog.objects.get(id= id)
    tags = Tag.objects.all().filter(blog = blog)
    category = Category.objects.all()
    recent_posts = Blog.objects.all().order_by('created_at')[:5]
    comments = Comment.objects.all().filter(blog= blog).order_by("time")[:5]
    
    if request.method == "POST":
        cm_form = CommentForm(request.POST)
        print("+")
        print("+")
        print(cm_form)
        print("+")
        print("+")
        if cm_form.is_valid():
            name = cm_form.cleaned_data['name']
            email = cm_form.cleaned_data['email']
            comment = cm_form.cleaned_data['comment']
            
            new_cm = Comment(blog= blog ,name= name, email= email, comment= comment)
            new_cm.save()
        
    
    context = {
        'blog': blog,
        'categories': category,
        'tags': tags,
        'recent_posts': recent_posts,
        'comment': comments,
    }
    
    return render(request, 'blogs/blog-details.html', context)

def blog_tag(request, tag):
    blog = Blog.objects.filter(tags__slug= tag)
    
    context = {
        'blogs': blog
    }
    
    return render(request, 'blogs/blog.html', context)




def blog_category(request, category):
    blog = Blog.objects.filter(category__slug= category)
    
    context = {
        'blogs': blog
    }
    
    return render(request, 'blogs/blog.html', context)

def search(request):
    if request.method == 'GET':
        q = request.GET.get("search")
        blogs = Blog.objects.filter(title__icontains= q )
        return render(request, 'blogs/blog.html', {'blogs':blogs})