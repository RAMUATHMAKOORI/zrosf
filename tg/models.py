from django.db import models

# Create your models here.
class std(models.Model):
    year=models.IntegerField()
    name=models.CharField(max_length=100)
    phone = models.BigIntegerField()