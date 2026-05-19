from django.contrib import admin
from .models import Airport, Trip


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "city", "country")
    search_fields = ("name", "code", "country")
    list_filter = ("country",)
    ordering = ("name",)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "baggage_name",
        "phone",
        "departure",
        "arrival",
        "date",
        "short_link",
    )
    search_fields = (
        "baggage_name",
        "phone",
        "departure__name",
        "departure__code",
        "arrival__name",
        "arrival__code",
    )
    list_filter = ("date", "departure", "arrival")
    autocomplete_fields = ("departure", "arrival")
    ordering = ("-date",)