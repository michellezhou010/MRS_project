#encoding:utf8
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)     #user name
    upwd = models.CharField(max_length=40)      #password
    uemail = models.CharField(max_length=30)    #email
    ushou = models.CharField(max_length=20, default='0')     #receiver    #default set
    uaddress = models.CharField(max_length=100, default='00') #address
    uyoubian = models.CharField(max_length=6, default='000000')   #postcode
    uphone = models.CharField(max_length=11, default='999999999')    #phone
    def __str__(self):
        return self.uname
    
    class Meta:
        db_table = "userinfo"
        verbose_name = 'userinfo'
        verbose_name_plural = 'userinfo'