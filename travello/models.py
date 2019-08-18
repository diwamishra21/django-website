from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length =100)
    image = models.ImageField(upload_to = 'pics')
    description = models.TextField()
    price = models.IntegerField()
    is_offer = models.BooleanField(default = False)
    class Meta:
        managed = True
        db_table = 'travello'


class Contact(models.Model):
    name = models.CharField(max_length =100)
    email= models.EmailField()
    mobile = models.CharField(max_length =100)
    message = models.TextField()
    class Meta:
        managed = True
        db_table = 'contact'