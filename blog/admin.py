from django.contrib import admin

# Register your models here.
from blog import models

class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", 'created')

admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Post, PostModelAdmin)


