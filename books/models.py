from django.db import models
from core import models as core_models


class Book(core_models.TimeStampedModel, core_models.Contents):

    """ Book Model Definition """

    writer = models.ForeignKey(
        "people.Person",
        related_name="books",
        on_delete=models.SET_NULL,
        null=True,
    )
    publication_date = models.TimeField()  # yyyy-mm-dd
    category = models.ForeignKey(
        "categories.Category",
        related_name="books",
        on_delete=models.SET_NULL,
        null=True,
    )
    cover_image = models.ImageField(blank=True)
    summary = models.TextField(default="")

    def __str__(self):
        return self.title