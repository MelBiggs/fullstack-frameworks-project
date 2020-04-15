from django.contrib import admin
from .models import Favourite

class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    

# Register your models here.
admin.site.register(Favourite, FavouriteAdmin)
