from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'slug', 'criado_em']
    prepopulated_fields = {'slug': ('titulo',)}
    list_filter = ['criado_em', 'autor']
    search_fields = ['titulo', 'conteudo']