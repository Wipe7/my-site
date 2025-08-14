from django.views.generic import TemplateView
from .models import Post
from django.shortcuts import render

class PostView(TemplateView):
    template_name = 'index.html'

def list_posts(request):
    posts = Post.objects.filter(status='published').order_by('-created_on')
    return render(request, 'post_detail.html', {'posts': posts})
