from django.db import models

# Create your models here.
class Cloths(models.Model):
    cloth_id=models.AutoField(auto_created=True,primary_key=True)
    cloth_name=models.CharField(max_length=200)
    cloth_type=models.CharField(max_length=200)
    cloth_details=models.CharField(max_length=200)
   
    cloth_price=models.CharField(max_length=500)
    
    class Meta:
        db_table="cloths"
