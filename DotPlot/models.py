from django.db import models

class Patients(models.Model):
    patientID = models.IntegerField(primary_key=True)
    patientName = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    history = models.BooleanField(default=False)
    scanID = models.IntegerField()

    def __str__(self):
        return self.patientName


class USscans(models.Model):
    scanID = models.IntegerField(primary_key=True)
    coordinates = models.CharField(max_length=2)
    scanDate = models.DateField()
    diagnosis = models.CharField(max_length=10)

    def __str__(self):
        return f"Scan ID: {self.scanID}"


