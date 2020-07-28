from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=200)
    
    admin=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    ) #Built-in User model that Django provides for authentication
    members=models.ManyToManyField(get_user_model())
    comments=models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])