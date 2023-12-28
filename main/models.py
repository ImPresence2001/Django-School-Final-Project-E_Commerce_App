from django.db import models

# Create your models here.

class Part(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    
class Software(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    
class Prebuild(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'