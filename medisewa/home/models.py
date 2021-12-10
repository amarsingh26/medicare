from django.db import models

# Create your models here.
class Signup(models.Model):
    firstname=models.CharField( max_length=200)
    lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    Email =models.EmailField(max_length=254)
    password=models.CharField(max_length=200)
    confirmpass=models.CharField(max_length=200)