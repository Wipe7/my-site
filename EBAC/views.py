from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post  # Agora o modelo Post existe

def home(request):
    return render(request, 'home.html')

class PostView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = 'posts'