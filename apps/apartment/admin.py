from django.contrib import admin

# Register your models here.
from apps.apartment.models import *

admin.site.register(ApartmentModel)
admin.site.register(Tags)
admin.site.register(Comment)