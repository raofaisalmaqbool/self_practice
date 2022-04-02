from django.contrib import admin
from myapp.models import Service
from myapp.models import *


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    # list_display is neccessory write same word as it is
    list_display = ('service_icon', 'service_title', 'service_des')


admin.site.register(Service, ServiceAdmin)
