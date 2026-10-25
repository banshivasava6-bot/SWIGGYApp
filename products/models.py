from django.db import models


class Product(models.Model):
    restaurant = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_available = models.BooleanField(
        default=True
    )

    # Filter fields
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.0
    )

    delivery_time = models.PositiveIntegerField(
        default=30
    )

    is_pure_veg = models.BooleanField(
        default=False
    )

    has_offer = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name