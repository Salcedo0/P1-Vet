from django.db import models

# Create your models here.
class Pet(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='vet/images/')
    url = models.CharField(blank=True)
