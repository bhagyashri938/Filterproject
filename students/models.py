from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    date_of_birth=models.DateField(null=True)
    marks=models.DecimalField(max_digits=5, decimal_places=2,null=True)
    
    def __str__(self):
        return self.name
    
    