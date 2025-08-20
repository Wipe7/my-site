from django.http import HttpResponse, JsonResponse
import asyncio
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'core/home.html', {'posts': posts})

def detalhe_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'core/detalhe_post.html', {'post': post})

def api(request):
    return HttpResponse("API funcionando!")

async def http_call_async(num):
    await asyncio.sleep(1)
    return f"Chamado número {num} completado!"

async def contador_api(request):
    resultados = []
    for num in range(1, 6):
        resultado = await http_call_async(num)
        resultados.append(resultado)
    return JsonResponse({"resultados": resultados})
