from django.contrib import admin
from .models import Product, Tag


class TagAdminInline(admin.TabularInline):
    model = Tag


class ProductAdmin(admin.ModelAdmin):
    inlines = (TagAdminInline, )


# Register your models here.
admin.site.register(Product, ProductAdmin)
