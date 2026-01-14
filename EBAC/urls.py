from django.urls import path
from . import views

app_name = 'EBAC'  

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]