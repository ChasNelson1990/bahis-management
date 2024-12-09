from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    upazila_code = models.PositiveIntegerField(blank=True, null=True)
    upazila_name = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.upazila_name


class DeskVersion(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    desk_version = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.desk_version
