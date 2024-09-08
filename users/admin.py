from django.contrib import admin

from bahis_management.desk.models import Module
from users.models import Profile

# Register your models here.
admin.site.register(Module)
admin.site.register(Profile)
