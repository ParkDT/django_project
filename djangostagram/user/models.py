from django.db import models
from django.db.models.base import Model
# Create your models here.
class Dsuser(models.Model):
    user_id= models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    created_at=models.DateTimeField(auto_now_add=True)