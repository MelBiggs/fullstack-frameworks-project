from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Product, Tag, Review


class TagAdminInline(admin.TabularInline):
    model = Tag


class ProductAdmin(admin.ModelAdmin):
    inlines = (TagAdminInline, )
    list_display = ('name', 'description')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('body', 'approved')
    list_filter = (
        ('published_date', DateFieldListFilter),
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)