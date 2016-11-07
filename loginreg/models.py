from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
role_choice = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
    )
class UserProfile(models.Model):
    user= models.OneToOneField(User)
    role= models.CharField(choices=role_choice, null=True, blank=True, max_length=15)
    def __str__(self):
        return '%s' % (self.user)