from django.db import models

# Create your models here.


class Patient(models.Model):

    id = models.AutoField.auto_created(auto_created=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    age = models.IntegerField()
