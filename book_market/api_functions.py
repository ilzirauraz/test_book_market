from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import Author, Book, User
from .serialization import *
import datetime


def get_author_info():
    """Получение информации об авторах"""
    authors_obj = Author.objects.all()
    books_obj = Book.objects.all()
    books_serializer = BookSerializer(books_obj, many=True)
    result = []
    for author in authors_obj:
        books_obj = get_author_books(author.id)
        books_list = [BookSerializer(book).data for book in books_obj]
        fio = AuthorSerializer(author).data
        result.append({
            'fio': fio['fio'],
            'books': books_list,
            'books_count': len(books_serializer.data)})
    return {'result': result}


def get_books():
    """Получение списка книг"""
    books_obj = Book.objects.all()
    books_serializer = BookSerializer(books_obj, many=True)
    books = books_serializer.data
    result = {'books': books}
    return result


def get_author_books(author_id):
    books = Book.objects.filter(author_id=author_id)
    print(books)
    return books


def get_book_obj_by_name(book_name):
    book = Book.objects.get(name=book_name)
    return book


def get_admins_email():
    """Получение почт администраторов"""
    users = User.objects.all()
    emails = [user.email for user in users if user.is_staff]
    return emails


def send_email(username):
    """Отправка почты администраторам"""
    emails = get_admins_email()
    message = 'Пользователь ' + str(username) + 'заполнил заявку'
    send_mail(
        'Заполнена заявка',
        message,
        "Admin",
        emails,
        fail_silently=False
        )


def create_purchase_request(request):
    """Создание нового запроса"""
    purchase_request = request.data
    purchase_request._mutable = True
    book_name = purchase_request.get('book')
    new_data = {
        'username': 'user@gmail.com',
        'date': datetime.date.today(),
        'book':  get_book_obj_by_name(book_name),
        'user_phone': purchase_request.get('user_phone')
        }
    if 'comment' in purchase_request:
        new_data = purchase_request.get('comment')
    serializer = PurchaseRequestSerializer(data=new_data)
    if serializer.is_valid(raise_exception=True):
        result = serializer.create(new_data)
        send_email(new_data['username'])
        return {'status': 'success'}
    else:
        return {'status': 'faild'}


def is_user_exsist(username):
    """Проверка на существование пользователя с пришедшим логином"""
    user_obj = User.objects.filter(username=username)
    user_ser = UserSerializer(user_obj, many=True)
    user = user_ser.data
    if user:
        return True
    else:
        return False


def create_new_user(request):
    "Cоздание новго пользователя"
    user_data = request.data
    username = user_data['username']
    password = str(user_data['password'])
    if not is_user_exsist(username):
        user_data_base = {
            'username': username,
            'password': make_password(password)
            }
        serializer = UserSerializer(data=user_data_base)
        if serializer.is_valid(raise_exception=True):
            serializer.create(user_data_base)
        return {'status': 'success'}
    else:
        return {'status': 'user with this login already exists.'}
