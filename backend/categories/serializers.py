"""
Serializer to convert Catrgory Model instance
into JSON and vise versa
"""

from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
