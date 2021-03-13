from django.contrib import admin

from .models import Address, OpeningHour, Product, Store


class ProductInline(admin.StackedInline):
    model = Product
    extra = 0


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class OpeningHourInline(admin.StackedInline):
    model = OpeningHour
    extra = 0


class StoreAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
        AddressInline,
        OpeningHourInline,
    ]


admin.site.register(Store, StoreAdmin)
