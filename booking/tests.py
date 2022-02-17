from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse
from booking.views import booking_pannel,edit
from django.contrib.auth.models import User

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_booking(self):
        url=reverse("booking")
        self.assertEquals(resolve(url).func,booking_pannel)
    
    def test_case_bedit_url(self):
        url=reverse('bedit',args=[1])
        self.assertEquals(resolve(url).func,edit)
