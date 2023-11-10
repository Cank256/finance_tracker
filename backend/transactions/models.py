from djongo import models
from categories.models import Category

class Transaction(models.Model):
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
