from django.contrib import admin

# Register your models here.
from .models import Product



class ProductAdmin(admin.ModelAdmin):
	list_display=('title','id','price','max_resolution','main_image','speed',)#,'native_in_out')
	list_editable=('max_resolution',)
admin.site.register(Product, ProductAdmin)