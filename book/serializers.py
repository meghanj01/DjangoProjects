from .models import BooksModel
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'

