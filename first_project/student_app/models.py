from django.db import models

class Student(models.Model):
    roll = models.PositiveBigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    marks = models.FloatField()
    
