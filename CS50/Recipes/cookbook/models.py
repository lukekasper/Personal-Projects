from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

import re


# Create your models here.
class User(AbstractUser):
    pass


class Recipe(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, related_name="recipes")
    title = models.CharField(max_length=50, null=True)
    ingredients = models.CharField(max_length=5000, null=True, blank=True)
    instructions = models.CharField(max_length=50000, null=True, blank=True)
    sub_recipe = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="recipes_contain")
    category = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    cooktime = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=500, blank=True)
    user_rating = models.CharField(max_length=50000, null=True, blank=True)

    # make a dict object from user rating charfield
    def user_rating_dict(self):
        rating_dict = dict()
        if self.user_rating is not None:

            # get rid of {} and split by dict entry
            rating_str = self.user_rating[1:-1]
            ratings_list = rating_str.split(",")

            # loop through each entry and split into separate key: value pairs
            for entry in ratings_list:
                current_entry = entry.split(":")

                # trim off extra characters from converting between string and dictionary types
                username = current_entry[0].strip()
                rating = current_entry[1].strip()
                start_ind, end_ind = 0, len(username) - 1
                if re.search(r"[a-zA-Z0-9_]", username) is not None:
                    res1 = re.search(r"[a-zA-Z0-9_]", username)
                    res2 = re.search(r"[a-zA-Z0-9_]", username[::-1])
                    start_ind, end_ind = res1.start(), res2.start()
                rating_dict[username[start_ind:len(username) - end_ind]] = int(rating)

        return rating_dict

    # get the avaerage value of the user ratings for display
    def avg_rating(self):
        if self.user_rating_dict():
            return round(sum(self.user_rating_dict().values())/len(self.user_rating_dict().values()), 1)
        else:
            return 0

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "poster": self.user.username,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "category": self.category,
            "image": self.image.url,
            "cooktime": self.cooktime,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "note": self.note,
            "rating": self.avg_rating()
        }


class RecipesForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ["title", "ingredients", "instructions", "category", "image", "cooktime", "note"]