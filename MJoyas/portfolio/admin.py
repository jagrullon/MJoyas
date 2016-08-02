from django.contrib import admin
from . import models

class HeaderAdmin(admin.ModelAdmin):
	model = models.HomeHeader
	list_display = ('title', 'header',)

admin.site.register(models.HomeHeader, HeaderAdmin)

class BrandAdmin(admin.ModelAdmin):
	model = models.Brand
	list_display = ('brand_name',)
	prepopulated_fields = {'slug' : ('brand_name',)}

admin.site.register(models.Brand, BrandAdmin)