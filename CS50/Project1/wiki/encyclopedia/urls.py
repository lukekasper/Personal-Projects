from django.urls import path
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("Search", views.search, name="search"),
    path("Create New Page", views.new_page, name="new_page"),
    path("Edit Content", views.edit_page, name="edit_page"),
    path("Random", views.random_page, name="random_page"),
    path("<str:title>", views.entry_page, name="entry"),
]
