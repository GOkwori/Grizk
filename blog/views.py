from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages  # Import for messaging framework
from .models import Blog
from .forms import BlogForm


def blog_list(request):
    """
    View to display a list of all published blog posts.
    """
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    """
    View to display a detailed view of a single blog post.
    """
    blog = get_object_or_404(Blog, id=blog_id)
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
            blog.author = request.user  # Set the author to the logged-in user
            blog.save()
            # Success message
            messages.success(request, "Blog post created successfully!")
            return redirect(reverse('blog_detail', args=[blog.id]))  # Redirect to blog_detail after saving
        else:
            messages.error(
                request, "Error creating blog post. Please check the form.")
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

    # Ensure that only the author or an admin can edit
    if request.user != blog.author and not request.user.is_superuser:
        messages.warning(
            request, "You are not allowed to edit this blog post.")
        return HttpResponseForbidden("You are not allowed to edit this blog post.")

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Blog post updated successfully!")
            return redirect('blog_detail', blog_id=blog.id)
        else:
            messages.error(
                request, "Error updating blog post. Please check the form.")
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    return render(request, 'blog/blog_form.html', {'form': form, 'blog': blog})


@login_required
def delete_blog(request, blog_id):
    """
    View to delete a blog post.
    Only accessible by the blog's author or an admin user.
    """
    blog = get_object_or_404(Blog, id=blog_id)

    # Ensure that only the author or an admin can delete
    if request.user == blog.author or request.user.is_superuser:
        blog.delete()
        # Success message
        messages.success(request, "Blog post deleted successfully!")
        return redirect('blog_list')

    messages.warning(request, "You are not allowed to delete this blog post.")
    return HttpResponseForbidden("You are not allowed to delete this blog post.")


@login_required
def blog_dashboard(request):
    """ A view to return the admin dashboard """

    if not request.user.is_superuser:
        messages.warning(
            request, "You do not have permission to access this page.")
        return HttpResponseForbidden("You do not have permission to access this page.")

    return render(request, 'blog/blog_dashboard.html')
