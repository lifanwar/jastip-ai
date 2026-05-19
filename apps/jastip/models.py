from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Trip(models.Model):
    baggage_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    departure = models.ForeignKey(Airport, on_delete=models.RESTRICT, related_name="departure_trips")
    arrival = models.ForeignKey(Airport, on_delete=models.RESTRICT, related_name="arrival_trips")
    date = models.DateTimeField()
    short_link = models.URLField()