from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('F', 'Face'),
    ('B', 'Body'),
    ('BL', 'Blog')
)

LABEL_CHOICES = (
    ('EC', 'Eczema'),
    ('PS', 'Psoriasis'),
    ('AC', 'Acne'),
    ('RO', 'Rosacea'),
    ('D', 'Dry Skin'),
    ('O', 'Oily Skin'),
    ('S', 'Sensitive'),
    ('TI', 'Tired Skin'),
    ('AG', 'Aging Skin'),
    ('AL', 'Alopecia'),
    ('PR', 'Pregnancy'),
    ('CE', 'Cellulite'),
    ('SC', 'Scarring'),
    ('SU', 'Sun')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

    
class Product(models.Model):

    name = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='F')
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Tag(models.Model):
    product = models.ForeignKey(Product, related_name="tags", related_query_name="tag")
    value = models.CharField(choices=LABEL_CHOICES, max_length=2)


class Review(models.Model):
    title = models.CharField(max_length=254, default='')
    body = models.TextField()
    score = models.IntegerField()
    approved = models.BooleanField(default=False)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE, related_query_name="review", null=True)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE, related_query_name="review", null=True)
