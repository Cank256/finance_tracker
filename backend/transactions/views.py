from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from categories.models import Category

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
