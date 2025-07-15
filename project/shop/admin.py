from django.contrib import admin

from .models import BookProduct, Author, Category

# Register your models here.


@admin.register(BookProduct, Author, Category)
class IndexShop(admin.ModelAdmin):
    pass
