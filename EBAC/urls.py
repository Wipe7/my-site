from django.urls import path
from .views import post
from EBAC import views

urlpatterns = [
    path("", views.PostView.as_view(), name="home"), 
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
