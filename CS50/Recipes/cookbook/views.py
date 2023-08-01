import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Recipe, Comment


def login_view(request):
    """
    Handles the user login process. If the request method is POST, it attempts
    to authenticate the user using the provided username and password. If the authentication
    is successful, the user is logged in and redirected to the "index" page. If the
    authentication fails, the login page is re-rendered with an error message.

    If the request method is not POST, it simply renders the login page.
    """
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
    """
    Logs out the currently authenticated user by using the Django built-in
    `logout` function. After logging out, the user is redirected to the "index" page.
    """
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


@login_required
def new_recipe(request):
    return render(request, "cookbook/new_recipe.html")


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

        # add ingredients and directions
        ingredients = list(request.POST.get("ingredients").split(","))
        ingredients_str = ''
        for ingredient in ingredients:
            ingredients_str += ingredient + ","
        ingredients_str = ingredients_str[:-1]
        directions = request.POST.get("instructions")

        # create recipe
        recipe = Recipe(user=user, title=title, ingredients=ingredients_str, directions=directions, category=category,
                        image=image, cooktime=cooktime)

        # add notes to recipe model if notes were uploaded, otherwise leave blank
        if request.POST.get("notes", False):
            notes = request.POST.get("notes")
        else:
            notes = ''
        recipe.note = notes

        # try to create recipie
        try:
            recipe.save()

        # catch issues with incomplete model fields
        except IntegrityError:
            # Handle the IntegrityError
            error_message = "Some required fields are missing. Please fill out all the required fields."
            return JsonResponse({"error": error_message}, status=400)

        HttpResponseRedirect("index")

    # For other request methods (e.g., GET, PUT, DELETE, etc.), return HTTP 405 Method Not Allowed
    error_message = "Only POST method is allowed for this URL."
    return HttpResponseNotAllowed(permitted_methods=["POST"], content=error_message)


def all_recipes(request):

    try:
        recipes = Recipe.objects.all()
        recipes = recipes.order_by("-timestamp").all()
        recipes_list = [recipe.serialize() for recipe in recipes]

        # set start and end points
        start = int(request.GET.get("start") or 0)
        end = int(request.GET.get("end") or (len(recipes) - 1))

        if start > len(recipes) - 1:
            recipes_list = []
        elif end > len(recipes) - 1:
            end = len(recipes) - 1
            recipes_list = recipes_list[start:end + 1]
        else:
            recipes_list = recipes_list[start:end + 1]

        # .serialize() creates a text string for json object
        return JsonResponse({"recipes": recipes_list})

    # Handle invalid input (e.g., non-integer values for start/end)
    except ValueError:
        return JsonResponse({"error": "Invalid input parameters."}, status=400)

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def get_recipe(request, name):

    # get requested recipe and set favorite flag
    try:
        recipe = Recipe.objects.get(title=name)
        favorite_flag = "None"

        # if the recipe is in the user's list of favorites, set favorite flag to True
        if request.user.is_authenticated:
            if recipe in request.user.favorites.all():
                favorite_flag = "True"
            else:
                favorite_flag = "False"

        return JsonResponse({"recipe": recipe.serialize(), "favorite_flag": favorite_flag})

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def update_rating(request, name):

    # ensure request was a PUT
    if request.method == "PUT":

        # get recipe info and convert user ratings into a dictionary
        recipe = Recipe.objects.get(title=name)

        try:
            rating_dict = recipe.user_rating_dict()
            signed_user = request.user.username
            data = json.loads(request.body)
            rating = data.get("rating")

            # check if rating is an int from 1-5
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                return JsonResponse({"error": "Invalid rating. Rating must be an integer between 1 and 5."}, status=400)

            # either add new entry or update existing entry and save
            rating_dict[signed_user] = data.get("rating")
            recipe.user_rating = str(rating_dict)

            recipe.save()
            return JsonResponse({"avg_rating": recipe.avg_rating(), "num_ratings": recipe.num_ratings()})

        # return error code if invalid JSON data
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in the request body."}, status=400)

        # return error code if any other exception occurs
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    error_message = "Only PUT method is allowed for this URL."
    return HttpResponseNotAllowed(permitted_methods=["PUT"], content=error_message)


@login_required
def search_recipes(request):

    # get ingredients list and split into individual ingredients
    # try reading the json data
    try:
        data = json.loads(request.body)
        search = data.get("search")

        recipes = Recipe.objects.all()
        matched_recipes = set()

        search_list = search.split(", ")

        # loop over all recipes
        for recipe in recipes:

            # clean the ingredients data
            recipe_ingredients_list = recipe.ingredients
            recipe_ingredients_list = recipe_ingredients_list[1:-1]
            recipe_ingredients_list = recipe_ingredients_list.replace('"', '')
            recipe_ingredients_list = recipe_ingredients_list.split(",")

            # if the recipe has the ingredients being searched, add it to the list of recipes to return
            if set(search_list).issubset(set(recipe_ingredients_list)):
                matched_recipes.add(recipe.title)

            # check if search matches a recipe title, if so add it to the matched recipes list
            if len(search_list) == 1:
                if search_list[0] in recipe.title:
                    matched_recipes.add(recipe.title)

        return JsonResponse({"matched_recipes": list(matched_recipes)})

    # return error code if invalid JSON data
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data in the request body."}, status=400)

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def my_recipes(request):

    try:
        # get signed-in user recipes posted by that user and order by post time
        user = request.user
        user_recipes = Recipe.objects.filter(user=user)
        user_recipes = user_recipes.order_by("-timestamp").all()

        # set start and end points
        start = int(request.GET.get("start"))
        end = start + 10
        total_recipes = len(user_recipes)

        # Clamp start and end to valid values
        start = max(min(start, total_recipes - 1), 0)
        end = max(min(end, total_recipes - 1), 0)

        # return appropriate recipes
        user_recipes = user_recipes[start:end]

        # .serialize() creates a text string for json object
        return JsonResponse({"user_recipes": [recipe.serialize() for recipe in user_recipes]})

    except ValueError:
        # Handle invalid input (e.g., non-integer values for start/end)
        return JsonResponse({"error": "Invalid input parameters."}, status=400)

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def cuisines(request):

    # try loading cuisines
    try:
        recipes = Recipe.objects.all()
        cuisines_list = set()

        for recipe in recipes:
            cuisines_list.add(recipe.category)

        return JsonResponse({"list": list(cuisines_list)})

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def cuisine_recipes(request, cuisine):

    # try loading cuisine recipes
    try:
        recipes = Recipe.objects.filter(category=cuisine)
        recipes = recipes.order_by("-timestamp").all()

        # set start and end points
        start = int(request.GET.get("start"))
        end = start + 10
        if start > len(recipes) - 1:
            start = len(recipes) - 1
            end = len(recipes) - 1
        elif end > len(recipes) - 1:
            end = len(recipes) - 1

        # return appropriate recipes
        recipes = recipes[start:end]

        # .serialize() creates a text string for json object
        return JsonResponse({"cuisine_recipes": [recipe.serialize() for recipe in recipes]})

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def favorites(request):

    # try loading favorite recipes
    try:
        # get recipes favorited by signed in user
        recipes = request.user.favorites.all()

        # .serialize() creates a text string for json object
        return JsonResponse({"list": [recipe.serialize() for recipe in recipes]})

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def update_favorites(request, title):

    # ensure method was a PUT request
    if request.method == "PUT":

        # try to get signed-in user, recipe to update, and flag from PUT request
        try:
            user = request.user
            recipe = Recipe.objects.get(title=title)

            # update user's favorites according to flag logic
            if recipe in user.favorites.all():
                user.favorites.remove(recipe)
                flag = "False"
            else:
                user.favorites.add(recipe)
                flag = "True"
            user.save()

            return JsonResponse({"flag": flag})

        # return error code if any other exception occurs
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    error_message = "Only PUT method is allowed for this URL."
    return HttpResponseNotAllowed(permitted_methods=["PUT"], content=error_message)


@login_required
def add_comment(request, title):

    if request.method == "POST":

        # get recipe, user, and comment info
        user = request.user
        recipe = Recipe.objects.get(title=title)
        data = json.loads(request.body)
        text = data.get("comment")

        # create new comment object
        comment = Comment(text=text, user=user, recipe=recipe)
        comment.save()

        return JsonResponse({"comment": comment.serialize()})

    return JsonResponse({"message": "Post Error."}, status=404)


@login_required
def remove_comment(request, id):

    # get comment by id and delete from database
    try:
        if Comment.objects.get(id=id):
            comment = Comment.objects.get(id=id)
            if comment.user != request.user:  # Assuming you have an 'author' field in the Comment model
                return JsonResponse({"message": "You are not authorized to delete this comment."}, status=403)
            comment.delete()
        return JsonResponse({"message": "Comment Removed."}, status=204)

    # return error if comment does not exist
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Comment not found."}, status=404)

    # return error code if any other exception occurs
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



