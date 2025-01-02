from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# View for listing all posts
def post_list(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'posts/post_list.html', {'posts': posts})

# View for displaying a single post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Fetch the post by ID or 404 if not found
    return render(request, 'posts/post_detail.html', {'post': post})

# View to create a new post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author as the current user
            post.save()
            return redirect('post_list')  # Redirect to the post list page after saving
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

# View to edit an existing post
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)  # Redirect to the post detail page after saving
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})
# View to delete a post
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # Redirect to the post list after deletion
    return render(request, 'posts/post_confirm_delete.html', {'post': post})