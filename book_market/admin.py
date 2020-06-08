from django.contrib import admin
from .models import User, Author, Book, PurchaseRequest


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(PurchaseRequest)
