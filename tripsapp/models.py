from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#Trips have an id, title, description, and image
class Trips(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey('auth.User', related_name='trips', on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', default="https://pngimage.net/wp-content/uploads/2018/06/profile-avatar-png-6.png", null=True, blank= True)
    bio =  models.TextField(default="", null=True, blank= True)
    def __str__(self):
        return self.user.username
