from django.db import models

# Create your models here.

class Livros(models.Model):
  title = models.CharField(max_length = 255) 
  author = models.CharField(max_length=255)
  release_year = models.DateField()
  description = models.TextField()
  created_at = models.DateField()
  active = models.BooleanField()
  
  def __str__(self):
      return self.title
  
  class Meta:
      verbose_name_plural = 'Livros'  