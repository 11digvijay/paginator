from django.db import models

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.fname}'