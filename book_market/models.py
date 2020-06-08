from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    fio = models.CharField(max_length=255)

    def __str__(self):
        return self.fio


class Book(models.Model):
    author = models.ForeignKey(
        'Author',
        related_name='books',
        on_delete=models.CASCADE,
        null=True
        )
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class PurchaseRequest(models.Model):
    book = models.ForeignKey(
        'Book',
        related_name='purchase_requests',
        on_delete=models.CASCADE,
        null=True,
        )
    username = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=11)
    comment = models.TextField(blank=True)
    date = models.CharField(max_length=255)
