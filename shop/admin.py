from django.contrib import admin

from .models import *
class categoryadmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
admin.site.register(category,categoryadmin)
admin.site.register(product)
admin.site.register(cart)
