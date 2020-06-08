from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication 
from .models import Author, Book
from .serialization import AuthorSerializer
from .api_functions import * 


class AuthorView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        author_info = get_author_info()
        return Response(author_info)

class BookView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        books = get_books()
        return Response(books)

class PurchaseRequestView(generics.CreateAPIView):
    serializer_class = PurchaseRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        result = create_purchase_request(request)
        return Response(result)

class RegistrationView(APIView):
    def post(self, request):
        result = create_new_user(request)
        return Response(result)
