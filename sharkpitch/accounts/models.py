from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class login(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=225)
    password=models.CharField(max_length=32)

class Signin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=225)
    password=models.CharField(max_length=100)

    #def save(self, *args, **kwargs):
        # Hash the password before saving
        #if self.pk is None:  # Only hash if it's a new instance
            #self.password = make_password(self.password)
        #super(Signin, self).save(*args, **kwargs)

class startup_register1(models.Model):
    SRNnumber = models.CharField(unique=True,max_length=9)
    Doc=models.ImageField(upload_to="media/images")

class startup_register2(models.Model):
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)
    q3 = models.CharField(max_length=250)
    q4 = models.CharField(max_length=250)
    q5 = models.CharField(max_length=250)
    q6 = models.CharField(max_length=250)
    q7 = models.CharField(max_length=250)
    q8 = models.CharField(max_length=250)


class startup_register3(models.Model):
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)
    q3 = models.CharField(max_length=250)

class startup_register4(models.Model):
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)

class startup_register5(models.Model):
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)


class startup_register6(models.Model):
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)


class startup_register7(models.Model):
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)

class startup_register8(models.Model):
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)
    q3 = models.CharField(max_length=250)
   
class startup_register10(models.Model):
    video = models.FileField(upload_to = 'media/videos')
