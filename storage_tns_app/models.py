from django.db import models
from datetime import datetime
from django.db.models.fields import AutoField
class user(models.Model):
    Username = models.CharField(primary_key=True,max_length=20)
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Username
    
class material(models.Model):
    order = models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID')
    Material = models.CharField(max_length=50)
    Amount = models.IntegerField()
    Picture = models.ImageField(upload_to='pictures/Material', blank=True)
    def __str__(self):
        return self.Material
    
class equipment(models.Model):
    order = models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID')
    Equipment = models.CharField(max_length=50)
    Amount = models.IntegerField()
    Picture = models.CharField(max_length=4000000, blank=True)
    def __str__(self):
        return self.Equipment
    

class history(models.Model):
    order = models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID')
    Equipment = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    Action = models.CharField(max_length=50)
    DateTime = models.DateTimeField(default=datetime.now, blank=True)
    Amount = models.IntegerField()
    def __str__(self):
        return self.Equipment
# Create your models here.
