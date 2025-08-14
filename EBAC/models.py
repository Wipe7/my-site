from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)   
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, default='sem-slug')
    status = models.CharField(max_length=10, choices= STATUS_CHOICES, default='draft')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title