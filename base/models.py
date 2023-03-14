from django.db import models

# Create your models here.
class Prices(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
class Portofolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.name