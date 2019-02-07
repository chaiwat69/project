from django.contrib import admin
from myapp.models import Product

class ProductAdmin(admin.ModelAdmin):
	field = ('name','price','category','image')
admin.site.register(Product,ProductAdmin)
