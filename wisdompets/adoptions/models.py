from django.db import models

# Create your models here.

class Pet(models.Model):
    SELECT_GENDER = [('M','Male'),('F','Female')]
    name = models.CharField(max_length = 30)
    submitter = models.CharField(max_length = 30)
    species = models.CharField(max_length = 30)
    breed = models.CharField(max_length = 30, blank=True)
    description = models.TextField()
    gender = models.CharField(choices=SELECT_GENDER, max_length = 1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)



