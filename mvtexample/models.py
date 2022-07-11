from pyexpat import model
from django.db import models

class helloemp(models.Model):
    empname=models.CharField(max_length=100)
    empid=models.CharField(max_length=100)
    empdept=models.CharField(max_length=100)
    empphone=models.CharField(max_length=100)

