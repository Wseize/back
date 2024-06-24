from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username_field = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    favorite_stores = models.ManyToManyField('delivery.Store', related_name='favorited_by', blank=True)

    def __str__(self):
        return self.username
