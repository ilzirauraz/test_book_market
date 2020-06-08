from django.urls import path
from .views import *
app_name = "book_market"

urlpatterns = [
    path('authors/', AuthorView.as_view()),
    path('books/', BookView.as_view()),
    path('purchase_request/', PurchaseRequestView.as_view()),
    path('registration/', RegistrationView.as_view()),
]
