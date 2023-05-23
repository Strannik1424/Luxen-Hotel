from django.contrib import admin

from apps.hoteInfo.models import *

# Register your models here.
admin.site.register(HotelInfo)
admin.site.register(Sidebar)
admin.site.register(NewSteller)

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Menu, MenuAdmin)