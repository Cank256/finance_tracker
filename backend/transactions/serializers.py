"""
Serializer to convert Transaction Model instance
into JSON and vise versa
"""

from rest_framework import serializers
from .models import Transaction
from categories.serializers import CategorySerializer

class TransactionSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()
    class Meta:
        model = Transaction
        fields = '__all__'
