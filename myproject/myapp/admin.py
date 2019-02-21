from django.contrib import admin
from myapp.models import Product

class ProductAdmin(admin.ModelAdmin):
	field = ('name','price','category','image')
	list_display = ('name','price','category','image')
	list_filter = ('category','price')
	list_editable = ('price','category','image')
admin.site.register(Product,ProductAdmin)

