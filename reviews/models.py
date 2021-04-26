from django.db import models
from core import models as core_models


class Photo(models.Model):

    """ Photo Model Definition """

    review = models.ForeignKey(
        "Review",
        related_name="photos",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField()  # file = models.ImageField(upload_to="room_photos")
    caption = models.CharField(max_length=80)

    def __str__(self):
        return self.caption


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    RATING_CHOICES = (
        (0, "☆☆☆☆☆"),
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    )

    created_by = models.ForeignKey(
        "users.User",
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    contents = models.ForeignKey(
        "cores.Category",
        related_name="reviews",
        on_delete=models.SET_NULL,
        null=True,
    )
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    is_open = models.BooleanField(default=False)