from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .serializers import BookSerializer
from .models import BooksModel
from rest_framework import status

# Create your views here.
@api_view(['POST', 'GET'])
def books(request):
    if request.method == 'POST':
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'GET':
        books = BooksModel.objects.all()
        
        book_data = BookSerializer(books, many= True)
        return JsonResponse({'data':book_data.data}, safe= False)
        # return JsonResponse(book_data.errors, status = status.HTTP_404_NOT_FOUND)

@api_view(['PUT','DELETE','GET'])
def books_by_id(request, id):
    try:
        books = BooksModel.objects.get(id=id)
    except BooksModel.DoesNotExist:
        return JsonResponse({'message': 'The book doesnot exists'}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        books.delete()
        return JsonResponse({'message': ' Books deleted successfully'}, status = status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'GET':
        book_data = BookSerializer(books)
        return JsonResponse(book_data.data, safe= False)

