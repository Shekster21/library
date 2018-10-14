from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Catalogue(models.Model):
    BookNumber = models.IntegerField(unique=True)
    Title = models.CharField(max_length = 100)
    Author = models.CharField(max_length = 100)
    Category = models.CharField(max_length = 50)
    Pages = models.IntegerField()
    Publisher = models.CharField(max_length = 50)

    def __str__(self):
        return self.Title


class userInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    semester = models.IntegerField(default=1)
    batch = models.CharField(max_length=1,default='A')

    def __str__(self):
        return self.user.username

