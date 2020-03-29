from django.db import models


# Model for data from summary API
class Summary(models.Model):

    Country = models.CharField(max_length=255)
    Slug = models.CharField(max_length=255)
    NewConfirmed = models.IntegerField()
    TotalConfirmed = models.IntegerField()
    NewDeaths = models.IntegerField()
    TotalDeaths = models.IntegerField()
    NewRecovered = models.IntegerField()
    TotalRecovered = models.IntegerField()


