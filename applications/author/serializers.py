from rest_framework import serializers

from applications.author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'last_name', 'date_of_birth', 'place_of_birth')

