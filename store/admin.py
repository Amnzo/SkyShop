from django.contrib import admin
from .models import Address, Category, File, Image, Product, Cart, Order, ProductSale, Sale
from django.db.models import FileField
from .processors import resize_image
from django import forms

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'locality', 'city', 'state')
    list_filter = ('city', 'state')
    list_per_page = 10
    search_fields = ('locality', 'city', 'state')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',  'category_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ( 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}


class ProductAdmin(admin.ModelAdmin):
    print("chekinnnnngg image 00000000000000000000000000000000000000000000000")
    formfield_overrides = {
        FileField: {'widget': forms.ClearableFileInput},
    }
    def save_model(self, request, obj, form, change):
        print("chekinnnnngg image 01010------------------------")
        super().save_model(request, obj, form, change)
        print("chekinnnnngg imageIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        print(form.changed_data)
        if 'product_image' in form.changed_data:
            print("inside resize")
            resize_image(obj.product_image)
    list_display = ('title',  'category', 'product_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ( 'category', 'is_active', 'is_featured')
    list_filter = ('category', 'is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'category')
    prepopulated_fields = {"slug": ("title", )}

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user', 'product')


admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductSale)
admin.site.register(Sale)

admin.site.register(Image)


