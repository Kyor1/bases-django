from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
    # Campos
    rut = models.CharField(max_length=20, help_text="Enter field documentation")
    nombre_completo = models.CharField(max_length=20, help_text="Enter field documentation")
    def str(self):         
        return self.rut

class Cuenta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    saldo = models.IntegerField()
    

