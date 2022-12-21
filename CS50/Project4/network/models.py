from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="follower")
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="user_following")
    liked_posts = models.ManyToManyField("Post", symmetrical=False, blank=True, related_name="liked_posts")

    def serialize(self):
        return {
            "followers": [user.username for user in self.followers.all()],
            "following": [user.username for user in self.following.all()],
        }

    def count_followers(self):
        return self.followers.all().count()

    def count_following(self):
        return self.following.all().count()

    def return_liked_posts(self):
        return {
            "liked_posts": [post.id for post in self.liked_posts.all()]
        }


class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, related_name="posts")
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def serialize(self):
        return {
            "id": self.id,
            "poster": self.user.username,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes
        }

