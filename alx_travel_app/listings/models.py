from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

