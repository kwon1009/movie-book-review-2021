from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model Definition """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contents(models.Model):

    """ Contents Model Definition """

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"

    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
    )

    title = models.CharField(max_length=100)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)

    class Meta:
        abstract = True