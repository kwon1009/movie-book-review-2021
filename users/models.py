from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model Definition """

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGING_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(blank=True, null=True)
    nickname = models.CharField(max_length=10, null=True)
    about_me = models.TextField(blank=True, default="")
    login_method = models.CharField(
        max_length=10, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    my_list = models.ForeignKey(
        "lists.ReviewList",
        related_name="my_users",
        on_delete=models.SET_NULL,
        null=True,
    )
    fav_list = models.ForeignKey(
        "lists.ReviewList",
        related_name="fav_users",
        on_delete=models.SET_NULL,
        null=True,
    )
    wish_list = models.ForeignKey(
        "lists.ReviewList",
        related_name="wish_users",
        on_delete=models.SET_NULL,
        null=True,
    )
