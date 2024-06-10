from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=60)
    brand=models.CharField(max_length=60)
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    short_desc=models.CharField(max_length=300)
    long_desc=models.TextField()
    org_price=models.IntegerField()
    dis_price=models.IntegerField()
    img=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    heading = models.CharField(max_length=200)
    brief_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about_us_images/')
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # Add user field
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Add product field
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in {self.user.username}'s cart"
    
