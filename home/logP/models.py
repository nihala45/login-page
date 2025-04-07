from django.db import models





class CustomUser(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    otp_secret = models.CharField(max_length=200)
    otp_fld = models.CharField(max_length=70)
    is_blocked = models.BooleanField(default=False)