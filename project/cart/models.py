from django.db import models
from django.core.validators import MinValueValidator

from shop.models import BookProduct

# Create your models here.


class Order(models.Model):
    user = models.TextField()
    book_product = models.ForeignKey(BookProduct, on_delete=models.CASCADE, to_field='article')
    count = models.IntegerField(validators=[MinValueValidator(1)])

    def publish(self):
        self.save()

    @property
    def one_price(self):
        return self.count * self.book_product.price
