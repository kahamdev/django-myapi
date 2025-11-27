# we import admin from django.contrib
from django.contrib import admin

# we import AfricanLeaders model from django model
from .models import AfricanLeaders

# we reegister our models here.
admin.site.register(AfricanLeaders)
