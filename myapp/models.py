from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


# Create your models here.

class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=80)
    service_des = models.TextField()
    extra_text = HTMLField(null=True)


class News(models.Model):
    news_title = models.CharField(max_length=50)
    more_info = HTMLField()
    news_slug = AutoSlugField(populate_from='news_title', unique=True, null=True, default=None)
