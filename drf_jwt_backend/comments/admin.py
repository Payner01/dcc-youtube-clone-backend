import imp
from django.contrib import admin
from .models import Comments, Reply
# Register your models here.

admin.site.register(Comments, Reply)


