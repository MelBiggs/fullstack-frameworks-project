from django.db import models


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
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.name
