from django.db import models

class File(models.Model):

    creador = models.CharField(blank = False, max_length=50)
    clave = models.CharField(blank = False,max_length = 500)