from django.db import models

class File(models.Model):

    creador = models.CharField(blank = False, max_length=20)
    clave = models.CharField(blank = False)
    nombre = models.CharField(blank = False, max_length=25)