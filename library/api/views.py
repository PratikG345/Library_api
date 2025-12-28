from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import BookSerializer
from django.db.models import Q
from .models import Book

# Create your views here.
@api_view(['GET'])
def get_book(req):
    book = Book.objects.filter(Q(available=True) | Q(published_year=1989))
    serializer = BookSerializer(book, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_book(req):
    serializer = BookSerializer(data=req.data,many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def update_book(req,pk):
    book = get_object_or_404(Book,pk=pk)
    if req.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    if req.method == 'PUT':
        serializer=BookSerializer(book,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if req.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)