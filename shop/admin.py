from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.AboutUs)
admin.site.register(models.Cart)