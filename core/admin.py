from django.contrib import admin

from core import models

# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.AuthorProfile)
admin.site.register(models.Publisher)
admin.site.register(models.Order)
