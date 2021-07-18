from django.db import models


# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
def my_default():
    return {'foo': 'bar'}

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name = "user_profile", on_delete=models.CASCADE, primary_key=True, null = False)
    face_data = models.JSONField(default = my_default)
    


    @property
    def username(self):
        return self.user.username
 
    # Methods
 
    # Meta and String
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
        ordering = ("user",)
 
    def __str__(self):
        return self.user.username



