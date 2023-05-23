from django.contrib import admin

from .models import ContactModel, ContactModelForm
# Register your models here.

admin.site.register(ContactModel)
admin.site.register(ContactModelForm)