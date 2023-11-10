"""
Serializer to convert Transaction Model instance
into JSON and vise versa
"""

from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
