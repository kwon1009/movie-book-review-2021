from django.db import models
from core import models as core_models


class Movie(core_models.TimeStampedModel, core_models.Contents):

    """ Movie Model Definition """

    director = models.ForeignKey(
        "people.Person",
        related_name="director_movies",
        on_delete=models.SET_NULL,
        null=True,
    )
    casts = models.ManyToManyField(
        "people.Person",
        related_name="cast_movies",
        on_delete=models.SET_NULL,
        null=True,
    )
    opening_date = models.TimeField()  # yyyy-mm-dd
    category = models.ForeignKey(
        "categories.Category",
        related_name="movies",
        on_delete=models.SET_NULL,
        null=True,
    )
    poster = models.ImageField(blank=True)
    summary = models.TextField(default="")

    def __str__(self):
        return self.title