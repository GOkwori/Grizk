from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    """
    View to display a list of all published blog posts.
    """
    blogs = Blog.objects.filter(status='published').order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    """
    View to display a detailed view of a single blog post.
    """
    blog = get_object_or_404(Blog, id=blog_id, status='published')
    return render(request, 'blog/blog_detail.html', {'blog': blog})


@login_required
def add_blog(request):
    """
    View to create a new blog post.
    Only accessible by logged-in users.
    """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm()

    return render(request, 'blog/blog_form.html', {'form': form})


@login_required
def edit_blog(request, blog_id):
    """
    View to edit an existing blog post.
    Only accessible by the blog's author or an admin user.
    """
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.user != blog.author and not request.user.is_superuser:
        return redirect('blog_list')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})


@login_required
def delete_blog(request, blog_id):
    """
    View to delete a blog post.
    Only accessible by the blog's author or an admin user.
    """
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.user == blog.author or request.user.is_superuser:
        blog.delete()
    
    return redirect('blog_list')