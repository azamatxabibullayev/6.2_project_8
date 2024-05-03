from django.db import models


# Create your models here.

class BackendDev(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    skills = models.CharField(max_length=255)
    experience = models.IntegerField()

    class Meta:
        db_table = 'BackendDev'

    def __str__(self):
        return self.name
