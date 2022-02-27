from rest_framework import serializers

from applications.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book.objects.all()
        fields = '__all__'

