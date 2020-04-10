from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    list_display = ('full_name', 'date')
    list_filter = (
        ('date', DateFieldListFilter),
    )

admin.site.register(Order, OrderAdmin)
