from datetime import date as Date, datetime as DateTime
from typing import List, Optional

from django.utils import timezone
from ninja import Router, Schema
from ninja.errors import HttpError
from ninja.pagination import paginate

from .models import Trip


router = Router(tags=["Trips"])

class TripOut(Schema):
    id: int
    baggage_name: str
    phone: str
    departure: str
    arrival: str
    date: DateTime
    short_link: str

    @staticmethod
    def resolve_departure(obj):
        return str(obj.departure)

    @staticmethod
    def resolve_arrival(obj):
        return str(obj.arrival)


@router.get("/trips", response=List[TripOut])
@paginate
def search_trips(
    request,
    start_date: Date,
    end_date: Optional[Date] = None,
):
    today = timezone.localdate()

    if start_date < today:
        raise HttpError(
            400,
            "Tanggal pencarian tidak boleh kurang dari hari ini."
        )

    if end_date is not None and end_date < today:
        raise HttpError(
            400,
            "Tanggal akhir tidak boleh kurang dari hari ini."
        )

    if end_date is not None and start_date > end_date:
        raise HttpError(
            400,
            "start_date tidak boleh lebih besar dari end_date."
        )

    queryset = Trip.objects.select_related(
        "departure",
        "arrival",
    ).order_by("date")

    if end_date is None:
        queryset = queryset.filter(date__date=start_date)
    else:
        queryset = queryset.filter(
            date__date__gte=start_date,
            date__date__lte=end_date,
        )

    return queryset