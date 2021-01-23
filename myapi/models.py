from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

