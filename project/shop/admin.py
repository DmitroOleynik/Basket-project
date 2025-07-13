from django.contrib import admin

from .models import BookProduct, Author, Genre

# Register your models here.


@admin.register(BookProduct, Author, Genre)
class IndexShop(admin.ModelAdmin):
    pass
