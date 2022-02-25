from django.db import models
from datetime import datetime
from django.db.models.fields import AutoField
class user(models.Model):
    Username = models.CharField(primary_key=True,max_length=20)
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Username
    
class material(models.Model):
    order = models.AutoField(auto_created=True, primary_key=True)
    Material = models.CharField(max_length=50)
    Amount = models.IntegerField()
    Picture = models.ImageField(upload_to='material', blank=True)
    def __str__(self):
        return self.Material
    def delete(self):
        self.Picture.delete()
        super(material, self).delete()
    
class equipment(models.Model):
    order = models.AutoField(auto_created=True, primary_key=True)
    Equipment = models.CharField(max_length=50)
    Amount = models.IntegerField()
    Picture = models.ImageField(upload_to='equipment', blank=True)
    def __str__(self):
        return self.Equipment
    def delete(self):
        self.Picture.delete()
        super(equipment, self).delete()
    

class history(models.Model):
    order = models.AutoField(auto_created=True, primary_key=True)
    Equipment = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    Action = models.CharField(max_length=50)
    DateTime = models.DateTimeField(default=datetime.now, blank=True)
    Amount = models.IntegerField()
    Username = models.CharField(max_length=20, blank=True)
    def __str__(self):
       #History = str(self.Username ,self.Action ,self.Type ,self.Equipment ,self.Amount)
        History = self.Username+' '+self.Action +' '+self.Type +':'+self.Equipment +' (Amount:'+str(self.Amount)+')'
        return History
# Create your models here.
