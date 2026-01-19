from django.http import HttpResponse
from django.views import generic

from EBAC.views import post


class PostView(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"


class PostDetailView(generic.DetailView):
    model = PostView
    template_name = "post_detail.html"

