from django.db import models
from django.db.models import CASCADE

from applications.author.models import Author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=CASCADE, related_name='book')
    title = models.CharField(max_length=255)
    date_of_publish = models.DateTimeField()
    picture = models.ImageField(upload_to='media', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_bestseller = models.BooleanField()


    def __str__(self):
        return self.title

