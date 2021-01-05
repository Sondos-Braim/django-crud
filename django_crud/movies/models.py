from django.db import models
from django.urls import reverse
# Create your models here.
class Movie(models.Model):
    title= models.CharField(max_length=64)
    director= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rate= models.IntegerField()
    description= models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')