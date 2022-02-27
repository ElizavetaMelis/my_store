from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.books.models import Book
from applications.books.serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookView(APIView):
#     def get(self, request):
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def book_list(request):
#     if request.method == 'GET':
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True)
#         return Response(serializer.data)
