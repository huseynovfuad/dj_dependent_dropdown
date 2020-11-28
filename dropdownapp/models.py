from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Travel(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)