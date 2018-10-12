from django.db import models

class Employee(models.Model):
    idemployee = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.name
