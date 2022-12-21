import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Post


def index(request):
    return render(request, "network/index.html")


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
@csrf_exempt
def create_post(request):

    # Composing a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of the post
    data = json.loads(request.body)
    content = data.get("content", "")

    # get logged in user info to assign as "poster"
    name = request.user.username
    user = User.objects.get(username=name)

    # create post from user and json content
    post = Post(
        user=user,
        content=content,
    )
    post.save()

    return JsonResponse({"message": "Post successful."}, status=201)


def load_all_posts(request):

    # get all posts and order by chronological order
    posts = Post.objects.all()
    posts = posts.order_by("-timestamp").all()

    # signed-in user
    username = request.user.username

    [page_structure, num_pages] = paginate(posts)

    # .serialize() creates a text string for json object
    return JsonResponse({"page_structure": page_structure, "num_pages": num_pages, "signed_user": username})


def paginate(posts):

    # split list of posts into pages of 10 posts per page
    posts = [post.serialize() for post in posts]
    p = Paginator(posts, 10)
    page_structure = []

    # append each page object to a list of pages
    for i in range(1, p.num_pages+1):
        page_structure.append(p.page(i).object_list)

    return page_structure, p.num_pages


def profile_view(request, name):

    # get all post objects from user and send to profile html view
    profile_user = User.objects.get(username=name)
    posts = Post.objects.filter(user=profile_user)
    posts = posts.order_by("-timestamp").all()
    [page_structure, num_pages] = paginate(posts)

    # get the follower/following info for the user and prep for json object
    relations = profile_user.serialize()
    follow_info = {"relations": relations, "num_followers": profile_user.count_followers(),
                   "num_following": profile_user.count_following()}

    # determine if user is signed in
    if request.user.is_authenticated:
        signed_in = True
    else:
        signed_in = False

    # determine if profile user is signed in user
    if request.user.username == profile_user.username:
        no_button = True
    else:
        no_button = False

    # determine if signed-in user is following profile user
    followers_list = profile_user.serialize()['followers']
    if request.user.username in followers_list:
        following_flag = True
    else:
        following_flag = False

    # make object of user relations logic
    user_relations = {"signed_in": signed_in, "no_button": no_button, "following_flag": following_flag}

    # create Json object from posts and follower/following info
    user_info = {"signed_user": request.user.username, "profile_username": profile_user.username,
                 "page_structure": page_structure, "num_pages": num_pages, "follow_info": follow_info,
                 "user_relations": user_relations}

    return JsonResponse(user_info)


@csrf_exempt
@login_required
def add_follower(request):

    # Update follower/following info
    if request.method == "PUT":
        data = json.loads(request.body)
        signed_in_user = request.user
        if data.get("follow") is not None:
            prof_user = User.objects.get(username=data.get("follow"))

            # determine if signed-in user is in profile user's followers list
            followers_list = prof_user.serialize()['followers']
            if signed_in_user.username in followers_list:
                signed_in_user.following.remove(prof_user)
                prof_user.followers.remove(signed_in_user)
                signed_in_user.save()
                prof_user.save()
            else:
                signed_in_user.following.add(prof_user)
                prof_user.followers.add(signed_in_user)
                signed_in_user.save()
                prof_user.save()

        return HttpResponse(status=204)

    # User must be via PUT
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)


@login_required
def following_view(request):

    # get signed in user's followers
    following_list = request.user.serialize()['following']

    user = User.objects.get(username=following_list[0])
    all_posts = user.posts.all()

    # loop over followers list
    for i in range(len(following_list) - 1):

        # starting with second follower
        i += 1

        # for each follower in list, get all the posts and union it with the all_posts queryset
        user = User.objects.get(username=following_list[i])
        user_posts = user.posts.all()
        all_posts = all_posts | user_posts

    # order by inverse chronology
    all_posts = all_posts.order_by("-timestamp").all()
    [page_structure, num_pages] = paginate(all_posts)

    return JsonResponse({"page_structure": page_structure, "num_pages": num_pages,
                         "signed_user": request.user.username})


@login_required
def like_post(request, post_id):

    # get signed-in user and post
    user = request.user
    post = Post.objects.get(id=post_id)

    # get posts that the user liked
    user_liked_posts = user.return_liked_posts()

    # see if post_id is already liked by user
    if post_id in user_liked_posts["liked_posts"]:

        # remove it from posts the user likes
        user.liked_posts.remove(post)
        liked_flag = False

        # decrement the number of likes the post has
        post.likes -= 1

    # otherwise, do the opposite
    else:
        user.liked_posts.add(post)
        liked_flag = True
        post.likes += 1

    # save updates
    user.save()
    post.save()

    user_liked_posts = user.return_liked_posts()

    # return JsonResponse of logic to set color of liked button
    return JsonResponse({"liked_flag": liked_flag, "post": post.serialize()})


@csrf_exempt
@login_required
def edit_post(request, post_id):

    # Update follower/following info
    if request.method == "PUT":

        # get PUT request data
        data = json.loads(request.body)
        if data.get("content") is not None:

            # get post and update with PUT content
            post = Post.objects.get(id=post_id)
            post.content = data.get("content")
            post.save()

            # return JsonResponse({"message": "Update successful."}, status=201)
            return JsonResponse({"content": data.get("content")})

    # Request must be via PUT
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)
