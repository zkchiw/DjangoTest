from django.db import models

# Create your models here.

class SungJuk(models.Model):
 name = models.CharField(max_length=10)
 kor = models.IntegerField(default=0)
 eng = models.IntegerField(default=0)
 mat = models.IntegerField(default=0)
 sum = models.IntegerField(default=0)
 avg = models.IntegerField(default=0)
 grd = models.CharField(default='가', max_length=3)
 regdate = models.DateTimeField(auto_now_add=True)
