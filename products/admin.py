from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "price",
        "rating",
        "delivery_time",
        "food_type",
        "has_offer",
    )

    def food_type(self, obj):
        if obj.is_pure_veg:
            return "Veg"
        return "Non-Veg"

    food_type.short_description = "Food Type"