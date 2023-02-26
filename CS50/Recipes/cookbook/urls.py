from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_recipe", views.new_recipe, name="new_recipe"),

    # API routes
    path("add_recipe", views.add_recipe, name="add_recipe"),
    path("all_recipes", views.all_recipes, name="all_recipes"),
    path("recipe_page/<str:name>", views.get_recipe, name="recipe_page"),
    path("update_rating/<str:name>", views.update_rating, name="update_rating"),
    path("search_recipes", views.search_recipes, name="search_recipes")
]
