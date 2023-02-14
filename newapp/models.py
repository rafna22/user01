from django.db import models

# Create your models here.
class u_tab(models.Model):
	uname=models.CharField(max_length=100)
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	image=models.ImageField(upload_to='media/')

class contab(models.Model):
	name=models.CharField(max_length=100)
	subject=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=100)
	message=models.CharField(max_length=300)

class admin(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)		
	








