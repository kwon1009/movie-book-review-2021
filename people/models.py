from django.db import models
from core import models as core_models


class Person(core_models.TimeStampedModel):

    """ Person Model Definition """

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"

    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=10)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default="Writer")
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.name