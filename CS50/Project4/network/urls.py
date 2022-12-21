from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("posts", views.create_post, name="new_post"),
    path("posts/edit/<int:post_id>", views.edit_post, name="edit_post"),
    path("posts/all", views.load_all_posts, name="all_posts"),
    path("profile/<str:name>", views.profile_view, name="profile"),
    path("follower_relation", views.add_follower, name="follower_relation"),
    path("following", views.following_view, name="following"),
    path("like/<int:post_id>", views.like_post, name="like")
]
