from django.contrib import admin
from .models import Livros

# Register your models here.

class AdminLivros(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'created_at','author', 'active']
    search_fields = ['title']
    list_filter = ['active']
    list_display_links = ['title',]

admin.site.register(Livros, AdminLivros)

# title = models.CharField(max_length = 255) 
#   author = models.CharField(max_length=255)
#   release_year = models.DateField()
#   description = models.TextField()
#   created_at = models.DateField()
#   active = models.BooleanField()