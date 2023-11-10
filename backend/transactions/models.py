from django.db import models

class Transactions(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)
