from django.contrib import admin
from .models import Brand, Product

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo',)

admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'image', 'price',)
    list_display_links = ('image',)


admin.site.register(Product, ProductAdmin)





