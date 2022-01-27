from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id=models.AutoField(auto_created=True,primary_key=True)
    contact_name=models.CharField(max_length=200)
    contact_email=models.CharField(max_length=100)
    contact_phone=models.CharField(max_length=15)
    contact_message=models.TextField()
 

    class Meta:
        db_table="contact" 
