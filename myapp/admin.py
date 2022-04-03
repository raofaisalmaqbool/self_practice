from django.contrib import admin
from myapp.models import Service
from myapp.models import *


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    # this will dispaly this list as a table in penal
    # list_display is neccessory write same word as it is
    list_display = ('service_icon', 'service_title', 'service_des', 'extra_text')


class NewsService(admin.ModelAdmin):
    list_display = ('news_title', 'more_info')


admin.site.register(Service, ServiceAdmin)
admin.site.register(News, NewsService)
