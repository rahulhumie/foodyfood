from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models .EmailField()
    # address = models.TextField()
    # image =models.ImageField()
    # files = models.FileField()

    

    # file = models.FileField()
class Car(models.Model):
    car_name = models.CharField(max_length=100);
    speed = models.IntegerField(default =50)


    def __str__(self):
        return self.name  