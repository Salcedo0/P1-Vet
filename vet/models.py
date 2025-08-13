from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=100)  # Nombre de quien envía el mensaje
    text = models.TextField()  # Contenido del mensaje
    timestamp = models.DateTimeField(default=timezone.now)  # Hora de envío

    def __str__(self):
        return f"{self.sender}: {self.text[:30]}"