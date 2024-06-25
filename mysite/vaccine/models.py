from django.db import models

# Create your models here.
class Vaccine(models.Model):
    name=models.CharField("vaccine name",max_length=32)
    description=models.TextField(max_length=1024)
    number_of_dosage=models.IntegerField(default=1)
    intervel=models.IntegerField(default=0,help_text="pls provide interval in days")
    storage_temperature=models.IntegerField(null=True,blank=True,help_text="provide the temperature")
    minimun_age=models.IntegerField(default=0)
                               
    def __str__(self) -> str:
        return self.name                          