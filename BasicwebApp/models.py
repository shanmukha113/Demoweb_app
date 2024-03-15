from django.db import models
from datetime import date

# Create your models here.


class Form(models.Model):
	id=models.AutoField(primary_key=True)

	name=models.CharField(max_length=100)
	mail=models.EmailField()
	age=models.IntegerField()

	date_of_birth=models.DateField(null=True,blank=True)
