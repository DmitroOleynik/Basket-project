from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    biography = models.TextField()
    date_born = models.DateField(null=True)
    date_death = models.DateField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def publish(self):
        self.save()

    def __str__(self):
        return f"{self.title}"


class BookProduct(models.Model):
    article = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    count_pages = models.IntegerField(validators=[MinValueValidator(1)])
    pictures = models.BooleanField()

    def publish(self):
        self.save()

    def __str__(self):
        return f"{self.title} - {self.author}"
