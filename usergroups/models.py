from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class UserGroup(Group):
    users = []

    def __str__(self):
        return self.name