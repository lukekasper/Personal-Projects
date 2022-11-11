from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"


class Listing(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500)
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    image_url = models.CharField(max_length=10000)
    category = models.CharField(max_length=64, null=True)
    winner = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.title}"


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watch_items")
    watch_item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="users_watching")

    def __str__(self):
        return f"{self.watch_item}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.user} bids {self.bid} on {self.listing}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True)
