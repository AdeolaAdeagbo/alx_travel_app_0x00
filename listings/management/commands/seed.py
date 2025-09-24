from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.utils import timezone
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings, and reviews"

    def handle(self, *args, **kwargs):
        # Clear old data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()

        # Create sample listings
        listings = []
        for i in range(5):
            listing = Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description=f"This is the description for listing {i+1}",
                price_per_night=random.randint(50, 200),
                location=f"City {i+1}"
            )
            listings.append(listing)

        # Create sample bookings
        for i in range(10):
            Booking.objects.create(
                listing=random.choice(listings),
                user_name=f"User {i+1}",
                start_date=timezone.now().date(),
                end_date=(timezone.now() + timezone.timedelta(days=3)).date()
            )

        # Create sample reviews
        for i in range(10):
            Review.objects.create(
                listing=random.choice(listings),
                user_name=f"Reviewer {i+1}",
                rating=random.randint(1, 5),
                comment=f"This is a review {i+1}"
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
