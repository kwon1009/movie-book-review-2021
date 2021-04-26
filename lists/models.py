from django.db import models
from core import models as core_models


class ReviewList(core_models.TimeStampedModel):

    """ Contents List Model Definiton """

    KIND_MINE = "mine"
    KIND_LIKE = "fav"
    KIND_WISH = "wish"

    KIND_CHOICES = (
        (KIND_MINE, "My List"),
        (KIND_LIKE, "Favorite List"),
        (KIND_WISH, "Wish List"),
    )

    created_by = models.ForeignKey(
        "users.User",
        related_name="review_lists",
        on_delete=models.CASCADE,
    )
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)
    reviews = models.ForeignKey(
        "reviews.Review",
        related_name="review_lists",
        on_delete=models.CASCADE,
    )