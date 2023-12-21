from django.db import models
from adminapp.models import *

class Users(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    phn_no=models.IntegerField(default=0)
    country=models.CharField(max_length=10)

class Signin(models.Model):
    email=models.EmailField()
    Password=models.CharField(max_length=10)

class Signup(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.CharField(max_length=15)

class Review(models.Model):
    review=models.TextField()

class Comments(models.Model):
    user_details=models.ForeignKey(Signup,on_delete=models.CASCADE,null=True,blank=True)
    date_time=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    movie_details=models.ForeignKey(Movies,on_delete=models.CASCADE,null=True,blank=True)
    comment=models.TextField()
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    is_liked=models.BooleanField(default=False)
    is_disliked=models.BooleanField(default=False)

class Wishlist(models.Model):
    user_details=models.ForeignKey(Signup,on_delete=models.CASCADE,null=True,blank=True)
    movie_details=models.ForeignKey(Movies,on_delete=models.CASCADE) 