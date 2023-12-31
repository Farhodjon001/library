from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(User,default='',on_delete=models.CASCADE)
    isbn=models.CharField(max_length=13)
    price=models.DecimalField(max_digits=300,decimal_places=2)


    def __str__(self):
        return self.title