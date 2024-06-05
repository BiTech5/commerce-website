from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=60)
    brand=models.CharField(max_length=60)
    short_desc=models.CharField(max_length=300)
    long_desc=models.TextField()
    org_price=models.IntegerField()
    dis_price=models.IntegerField()
    img=models.ImageField(upload_to='image/')

