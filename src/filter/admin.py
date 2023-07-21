from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Filter)
admin.site.register(FilterExtra)