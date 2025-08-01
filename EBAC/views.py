from django.views.generic import TemplateView

class PostView(TemplateView):
    template_name = 'index.html'
