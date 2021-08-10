from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=100)

class Languages(models.Model):
    language_name = models.CharField(max_length=100)

class World(models.Model):
    CountryId = models.ForeignKey(Countries,on_delete=models.CASCADE)
    LanguagesId = models.ForeignKey(Languages, on_delete=models.CASCADE)
