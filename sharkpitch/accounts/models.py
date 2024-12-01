from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class login(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=225)
    password=models.CharField(max_length=32)

class SigninManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.password=password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password)


class Signin(AbstractBaseUser, PermissionsMixin,models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=225)
    password=models.CharField(max_length=100)
    profession=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10,null=True)
    user_type=models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = SigninManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    #def save(self, *args, **kwargs):
        # Hash the password before saving
        #if self.pk is None:  # Only hash if it's a new instance
            #self.password = make_password(self.password)
        #super(Signin, self).save(*args, **kwargs)

class startup_register1(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register1')
    SRNnumber = models.CharField(unique=True,max_length=9)
    Doc=models.ImageField(upload_to="media/images")

class startup_register2(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register2')
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)
    q3 = models.CharField(max_length=250)
    q4 = models.CharField(max_length=250)
    q5 = models.CharField(max_length=250)
    q6 = models.CharField(max_length=250)
    q7 = models.CharField(max_length=250)
    q8 = models.CharField(max_length=250)


class startup_register3(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register3')
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)
    q3 = models.CharField(max_length=250)

class startup_register4(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register4')
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)

class startup_register5(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register5')
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)


class startup_register6(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register6')
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)


class startup_register7(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register7')
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)

class startup_register8(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register8')
    q1 = models.CharField(max_length=250)
    q2 = models.CharField(max_length=250)
    q3 = models.CharField(max_length=250)
   
class startup_register10(models.Model):
    user = models.ForeignKey(Signin, on_delete=models.CASCADE, related_name='register10')
    video = models.FileField(upload_to = 'media/videos')
