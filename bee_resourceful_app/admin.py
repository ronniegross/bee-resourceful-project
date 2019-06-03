from django.contrib import admin
from .models import User, Resource

# Register your models here.
from django.contrib import admin


admin.site.register([User, Resource])