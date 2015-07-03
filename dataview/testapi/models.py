from django.db import models

# Create your models here.

class Sample1(models.Model):
    text = models.CharField(max_length=100)\

class Sample(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    samples = models.ManyToManyField(Sample1)

    @property
    def get_apply_values(self):
        return {'a': 1}

