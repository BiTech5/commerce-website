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