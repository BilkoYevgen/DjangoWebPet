from django.contrib import admin
from .models import Brand, Product, SliderImage, ProdImage, Basket
from django.utils.safestring import mark_safe


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo',)

    def display_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="75">')
        return None

    display_logo.short_description = 'Logo'


admin.site.register(Brand, BrandAdmin)

class ProdImageAdmin(admin.TabularInline):
    fk_name = 'product'
    model = ProdImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'gender', 'is_kids', 'price', 'is_published',)
    list_display_links = ('name',)
    list_editable = ('brand', 'gender', 'is_kids', 'price', 'is_published',)
    exclude = ('size',)
    list_filter = ('brand', 'gender',)
    inlines = [ProdImageAdmin, ]


admin.site.register(Product, ProductAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

    def display_slider(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return None

    display_slider.short_description = 'Image'


admin.site.register(SliderImage, SliderAdmin)

class ProdImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product', 'display_image',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return None

    display_image.short_description = 'Image'

admin.site.register(ProdImage, ProdImageAdmin)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0


# admin.site.register(Basket, BasketAdmin)