from django.db import models

class Procucto(models.Model):
    marca = models.CharField(max_length = 50)
    modelo = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits = 4, decimal_places = 2)
    artesanal = models.BooleanField()
    nacionalidad = models.CharField(max_length = 50, blank = True, null =True)
    creado = models.DateTimeField(auto_now_add = True)
    editado = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.marca

