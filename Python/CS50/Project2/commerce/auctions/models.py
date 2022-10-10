from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title}: ${self.current_price}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_info")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_item")
    bid = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.user} bids {self.bid}"
