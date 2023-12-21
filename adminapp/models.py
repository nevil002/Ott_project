from django.db import models


class Genre(models.Model):
    genrename=models.CharField(max_length=50)

class Movies(models.Model):
    name=models.CharField(max_length=15)
    genre_id=models.ForeignKey(Genre,on_delete=models.CASCADE,null=True,blank=True)
    year=models.IntegerField()
    rating=models.FloatField()
    discription=models.CharField(max_length=100,default='no_discription_found')
    Poster=models.ImageField(upload_to='imgfile',default='null.jpg')
    File=models.FileField(upload_to='videofile',default=False)
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)