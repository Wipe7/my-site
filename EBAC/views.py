from django.shortcuts import render
from .models import Post

def index(request):
   
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }
    
    return render(request, 'index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})