from django.test import TestCase
from .models import ride
from rest_framework.test import APITestCase



class Testmodel(TestCase):
    def test_ride(self,):
        Ride=ride.objects.create(
            id=1,pickup_loc="Test Pickup Location",dropoff_loc="Test Dropoff Location",status="requested"
        )

class RideAPITestCase(APITestCase):
    def setUp(self):
        ride.objects.create(
            rider_id=1,
            pickup_loc="Test Pickup Location",
            dropoff_loc="Test Dropoff Location",
            status="requested",
        )



