from django.db import models

# Create your models here.
class PatientDetail(models.Model):
    PatientID = models.IntegerField(primary_key=True,default=99999)
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=250)
    BloodImage = models.ImageField(upload_to='PatientBloodImage/')
    Result = models.CharField(max_length=250,default="NULL")
