from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.forms import ImageField


class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userid=models.IntegerField(default=1)
    fname= models.CharField(max_length=20,blank=True)
    lname = models.CharField(max_length=20, blank=True)
    profimg = models.ImageField(upload_to='profimg/',default='blank.png')
    location = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True, max_length=100)
    working = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.user.username
class post(models.Model):
    users = models.ForeignKey(profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    caption = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.users.user.username}-{self.id}"
class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follows = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'follows')

    def __str__(self):
        return f"{self.user} follows {self.follows}"