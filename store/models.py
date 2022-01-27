from django.db import models

# Create your models here.
class Cloths(models.Model):
    cloths_id=models.AutoField(auto_created=True,primary_key=True)
    cloths_name=models.CharField(max_length=200)
    cloths_type=models.CharField(max_length=200)
    cloths_details=models.CharField(max_length=200)
    cloths_price=models.CharField(max_length=500)
    cloths_image=models.FileField(upload_to='cloths_image')
    
    class Meta:
        db_table="store"
