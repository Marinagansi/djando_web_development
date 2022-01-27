from django.db import models
from store.models import Cloths
from customer.models import Customer

# Create your models here.
class Booking(models.Model):
    booking_id=models.AutoField(auto_created=True,primary_key=True)
    cloth=models.ForeignKey(Cloths,on_delete=models.CASCADE)
    consumer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    start_date=models.DateField()
    days=models.CharField(max_length=50)
    # name=models.CharField(max_length=50)
    class Meta:
        db_table="booking"
