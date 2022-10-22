from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("new listing", views.new_listing, name="new_listing"),
    path("register", views.register, name="register"),
    path("bid", views.place_bid, name="bid"),
    path("comment", views.add_comment, name="comment"),
    path("watchlist", views.watchlist_page, name="watchlist"),
    path("close listing/<str:title>", views.close, name="close_listing"),
    path("categories", views.categories_view, name="categories"),
    path("category items/<str:category>", views.category_items, name="category_items"),
    path("edit watchlist/<str:title>", views.process_watchlist, name="edit_watchlist"),
    path("listings/<str:title>", views.listing_page, name="listing")
]
