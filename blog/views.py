from django.shortcuts import render, get_object_or_404

from .models import Post

def home(request):
    list_posts = Post.objects.all()

    for post in list_posts:
        post.content = ' '.join(post.content.split()[:100]) + '...'
        
    return render(request, "blog/home.html", {'list_posts': list_posts})

def post(request, post_id):
    # Recuepra el objeto Post utilizando el post_id proporcionado
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post.html", {'post': post})
