from django.db import models

# Create your models here.
class cruddata(models.Model):
    ID = models.CharField(max_length=10, primary_key=True )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name
