from django.db import models


class familiar(models.Model):
    nombre = models.CharField(max_length=40)
    documento = models.IntegerField()
    fechanac = models.DateField()

    
    
# Create your models here.
