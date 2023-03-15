from django.db import models
from django.contrib.auth.models import User

class Price(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
class Portofolio_Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    subject = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    answered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at','-created_at']
    
    def __str__(self):
        if self.answer is not None:
            return str("Answered: "+self.subject[0:30])
        return str("New: "+self.subject[0:30])
     