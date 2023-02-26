import json
import re
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Recipe


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cookbook/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "cookbook/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "cookbook/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "cookbook/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "cookbook/register.html")


def index(request):
    return render(request, "cookbook/index.html")


@csrf_exempt
@login_required
def new_recipe(request):
    return render(request, "cookbook/new_recipe.html")


@csrf_exempt
@login_required
def add_recipe(request):

    # create recipe from POST info
    if request.method == "POST":

        # get recipe info from fetch
        title = request.POST.get("title")
        user = request.user
        category = request.POST.get("category")
        cooktime = request.POST.get("cooktime")

        # get image if one was uploaded, otherwise use stock image
        if request.FILES.get("image", False):
            image = request.FILES["image"]
        else:
            image = "images/no_image.jpeg"

        # create recipe
        recipe = Recipe(user=user, title=title, category=category, image=image, cooktime=cooktime)

        # add directions and notes to recipe model (if notes were uploaded, otherwise leave blank)
        directions = request.POST.get("instructions")
        if request.POST.get("notes", False):
            notes = request.POST.get("notes")
        else:
            notes = ''

        # see if any of the ingredients are a sub-recipe, if so add it as one and remove from ingredients
        ingredients = list(request.POST.get("ingredients").split(","))
        ingredients_str = ''
        for ingredient in ingredients:
            if Recipe.objects.filter(title=ingredient):
                sub_rec = Recipe.objects.get(title=ingredient)
                ingredients.remove(ingredient)
                recipe.sub_recipe.add(sub_rec)
            else:
                ingredients_str += ingredient + ","
        ingredients_str = ingredients_str[:-1]

        # update recipe details
        recipe.ingredients = ingredients_str
        recipe.instructions = directions
        recipe.note = notes
        recipe.save()

        HttpResponseRedirect("index")

    return JsonResponse({"message": "Post Error."}, status=404)


def all_recipes(request):

    recipes = Recipe.objects.all()
    recipes = recipes.order_by("-timestamp").all()

    # .serialize() creates a text string for json object
    return JsonResponse({"recipes": [recipe.serialize() for recipe in recipes]})


def get_recipe(request, name):

    recipe = Recipe.objects.get(title=name)
    return JsonResponse(recipe.serialize(), safe=False)


@csrf_exempt
@login_required
def update_rating(request, name):

    # get recipe info and convert user ratings into a dictionary
    recipe = Recipe.objects.get(title=name)
    rating_dict = recipe.user_rating_dict()
    signed_user = request.user.username
    data = json.loads(request.body)

    # either add new entry or update existing entry and save
    rating_dict[signed_user] = data.get("rating")
    recipe.user_rating = str(rating_dict)
    recipe.save()

    return JsonResponse({"avg_rating": recipe.avg_rating()})


@csrf_exempt
def search_recipes(request):

    # get ingredients list and split into individual ingredients
    if request.method == "POST":
        data = json.loads(request.body)
        ingredients = data.get("ingredients")
        searched_ingredients = ingredients.split(", ")

        recipes = Recipe.objects.all()
        matched_recipes = []

        # loop over all recipes
        for recipe in recipes:

            # clean the ingredients data
            recipe_ingredients_list = recipe.ingredients
            recipe_ingredients_list = recipe_ingredients_list[1:-1]
            recipe_ingredients_list = recipe_ingredients_list.replace('"', '')
            recipe_ingredients_list = recipe_ingredients_list.split(",")

            # if the recipe has the ingredients being searched, add it to the list of recipes to return
            if set(searched_ingredients).issubset(set(recipe_ingredients_list)):
                matched_recipes.append(recipe.title)

        return JsonResponse({"matched_recipes": matched_recipes})
