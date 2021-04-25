from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin Definition """

    fieldsets = UserAdmin.fieldsets + (
        (
            "More",
            {
                "fields": (
                    "avatar",
                    "login_method",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "avatar",
        "login_method",
        "is_staff",
    )

    list_filter = ("login_method",)
