from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, WatchList, Bid, Comment


class BidForm(forms.Form):
    bid = forms.DecimalField(label="", decimal_places=2, max_digits=7)


class CommentForm(forms.Form):
    comment = forms.CharField(label="", max_length=500)


def index(request):

    # if posting a new listing to index, get all info and create a new listing
    if request.method == "POST":
        title = request.POST["title"]
        user = request.user
        starting_price = request.POST["starting_bid"]
        description = request.POST["description"]
        url = request.POST["url"]
        category = request.POST["category"]
        listing = Listing(title=title, user=user, description=description, current_price=starting_price, image_url=url,
                          category=category, winner="None")
        listing.save()
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
        "heading": "Active Listings:"
    })


def listing_page(request, title, message=""):

    # get listing
    listing = Listing.objects.get(title=title)

    # get comments from that listing
    comments = Comment.objects.filter(listing=listing)

    # if user is not signed in, set flag to hide "add/remove watchlist" link
    if not request.user.is_authenticated:
        flag = 0

        return render(request, "auctions/listing.html", {
            "listing": listing,
            "login_flag": flag,
            "bid_form": BidForm(),
            "error": message,
            "comments": comments,
            "comment_form": CommentForm()
        })

    else:
        flag = 1

        # get user info and watchlist to check if current listing is in watchlist
        name = request.user.username
        user = User.objects.get(username=name)
        watch_item = user.watch_items.filter(watch_item=listing)

        # set necessary tags for "Add/Remove Watchlist" link
        if not watch_item:
            link_tag1 = "Add"
            link_tag2 = "to"
        else:
            link_tag1 = "Remove"
            link_tag2 = "from"

        # check to see if logged-in user is the same one who posted the listing
        if name == listing.user.username:
            close_listing = True
        else:
            close_listing = False

        return render(request, "auctions/listing.html", {
            "listing": listing,
            "login_flag": flag,
            "tag1": link_tag1,
            "tag2": link_tag2,
            "bid_form": BidForm(),
            "error": message,
            "option": close_listing,
            "username": name,
            "comments": comments,
            "comment_form": CommentForm()
        })


@login_required
def process_watchlist(request, title):

    # get listing and current user
    listing = Listing.objects.get(title=title)
    user = User.objects.get(username=request.user.username)

    # check to see if listing is in user's watchlist, add or remove accordingly
    watch_item = user.watch_items.filter(watch_item=listing)
    if not watch_item:
        watch_list_item = WatchList(user=user, watch_item=listing)
        watch_list_item.save()
    else:
        item = WatchList.objects.filter(user=user, watch_item=listing)
        item.delete()

    return HttpResponseRedirect(reverse("index"))


@login_required
def new_listing(request):
    return render(request, "auctions/create_listing.html")


@login_required
def place_bid(request):
    if request.method == "POST":
        form = BidForm(request.POST)

        # if input to form is valid, get info to add a bid
        if form.is_valid():
            amount = form.cleaned_data["bid"]
            title = request.POST["listing_title"]
            listing = Listing.objects.get(title=title)

            # entered bid must be larger than current item price to be registered, if not throw an error
            if amount > listing.current_price:
                user = User.objects.get(username=request.user.username)
                bid = Bid(user=user, listing=listing, bid=amount)
                bid.save()
                listing.current_price = amount
                listing.save()
                return listing_page(request, title)
            else:
                return listing_page(request, title, message="Error1")
        else:
            return listing_page(request, request.POST["listing_title"], message="Error2")
    else:
        return HttpResponseRedirect(reverse("index"))


@login_required()
def close(request, title):

    listing = Listing.objects.get(title=title)

    # find the user who placed the winding bid and add a winner to listing model
    highest_bid = listing.current_price
    bid = Bid.objects.get(listing=listing, bid=highest_bid)
    winner = bid.user.username
    listing.winner = winner
    listing.save()
    return listing_page(request, listing.title)


@login_required()
def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)

        # if input to form is valid, get info to add a bid
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            user = User.objects.get(username=request.user.username)
            title = request.POST["listing_title"]
            listing = Listing.objects.get(title=title)
            new_comment = Comment(user=user, listing=listing, comment=comment)
            new_comment.save()
            return listing_page(request, title)
        else:
            return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))


@login_required()
def watchlist_page(request):

    user = User.objects.get(username=request.user.username)
    return render(request, "auctions/watchlist.html", {
            "user": user,
            "watch_list": user.watch_items.all()
        })


def categories_view(request):
    listings = Listing.objects.all()
    categories_list = set()
    for listing in listings:
        categories_list.add(listing.category)
    return render(request, "auctions/categories.html", {
        "categories": categories_list
    })


def category_items(request, category):
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "category": category,
        "heading": category+"s"
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
