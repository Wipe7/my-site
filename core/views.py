from django.http import HttpResponse, JsonResponse
import asyncio

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
