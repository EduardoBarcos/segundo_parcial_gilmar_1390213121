from django.db import models
from django.contrib.auth.models import User

class Recurso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
