from django.contrib import admin
from .models import Product, Tag, Review


class TagAdminInline(admin.TabularInline):
    model = Tag


class ProductAdmin(admin.ModelAdmin):
    inlines = (TagAdminInline, )
    list_display = ('name', 'description')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)