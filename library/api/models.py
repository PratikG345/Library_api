from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    available = models.BooleanField()
    
    def __str__(self):
        return f"{self.title}-{self.published_year}"