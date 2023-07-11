from django.contrib import admin
from .models import Brand, Product
from django.utils.safestring import mark_safe


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo',)

    def display_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="75">')
        return None

    display_logo.short_description = 'Logo'


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    fields = ('image',)
    list_display = ('name', 'brand', 'display_image', 'gender', 'price',)
    list_display_links = ('name',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return None

    display_image.short_description = 'Image'


admin.site.register(Product, ProductAdmin)







