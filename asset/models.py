from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name="IDC名称")
    address = models.CharField(max_length=32, verbose_name="地点")
    count = models.IntegerField()
    price = models.CharField(max_length=20, verbose_name="价格")


class Asset(models.Model):
    name = models.CharField(max_length=32, verbose_name="IDC名称")