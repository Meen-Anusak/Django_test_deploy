from django.db import models

# Create your models here.


class User(models.Model):
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname
