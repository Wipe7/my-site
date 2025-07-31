from django.urls import path
from .views import post
from . import views

urlpatterns = [
    path("", views.home,(), name="home"), 
]
