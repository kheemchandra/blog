from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm

def check_blog_maalik(request, blog):
    if request.user != blog.maalik:
        raise Http404

def home(request):
    return render(request, 'blogs/home.html')

def blogs(request):
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)

@login_required
def create_blog(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.maalik = request.user
            new_blog.save()
            return redirect('blogs:blogs')
    context = {'form': form}
    return render(request, 'blogs/create_blog.html', context)

@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_maalik(request, blog)

    if request.method != 'POST':
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    context = {'form': form, 'blog_id': blog_id}
    return render(request, 'blogs/edit_blog.html', context)

