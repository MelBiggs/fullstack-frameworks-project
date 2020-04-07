from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


CATEGORY_CHOICES = (
    ('F', 'Face'),
    ('B', 'Body')
)

# Skin Issues - Searchable on the product page
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

# Product Types
TYPE_CHOICES = (
    ('C', 'Cleanser'),
    ('EX', 'Exfoliator'),
    ('SE', 'Serum'),
    ('M', 'Moisturiser'),
    ('SU', 'Sunscreen'),
    ('T', 'Toner'),
    ('FM', 'Face Mask'),
    ('E', 'Eye Cream'),
    ('CH', 'Chemical'),
)


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2,
                                default='F')
    description = models.TextField()
    product_type = models.CharField(choices=TYPE_CHOICES, max_length=2,
                                    default="M")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Tag(models.Model):
    product = models.ForeignKey(Product, related_name="tags",
                                related_query_name="tag", null=True)
    value = models.CharField(choices=LABEL_CHOICES, max_length=2)


class Review(models.Model):
    title = models.CharField(max_length=254, default='')
    body = models.TextField()
    score = models.IntegerField()
    approved = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    product = models.ForeignKey(Product, related_name="reviews",
                                on_delete=models.CASCADE,
                                related_query_name="review", null=True)
    user = models.ForeignKey(User, related_name="reviews",
                             on_delete=models.CASCADE,
                             related_query_name="review", null=True)
    
    class Meta:
        ordering = ['-published_date']
