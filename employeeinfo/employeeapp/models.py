from django.db import models


class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=200)
    esalary=models.IntegerField(max_length=50)
    edescription=models.CharField(max_length=200)

    def __str__(self):
        return self.ename


# Create your models here.
