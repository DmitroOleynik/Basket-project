from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    biography = models.TextField()
    date_born = models.DateField(blank=True, null=True)
    date_death = models.DateField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Category(models.Model):
    title = models.CharField(max_length=255)

    def publish(self):
        self.save()

    def __str__(self):
        return f"{self.title}"


class BookProduct(models.Model):
    class Language(models.TextChoices):
        UKRAINIAN = "UKR", "Українська"
        ENGLISH = "ENG", "Англійська"

    class Pictures(models.TextChoices):
        COLOR = "COL", "Кольорові"
        BLACK_WHITE = "BW", "Чорно-білі"
        WITHOUT = "NON", "Відсутні"

    article = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    photo = models.ImageField(upload_to="img", null=True)
    language = models.CharField(max_length=3, choices=Language, default=Language.UKRAINIAN)
    count_pages = models.IntegerField(validators=[MinValueValidator(1)])
    pictures = models.CharField(max_length=3, choices=Pictures, default=Pictures.WITHOUT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return f"{self.title} - {self.author}"
