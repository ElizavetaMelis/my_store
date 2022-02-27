from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.author.models import Author
from applications.author.serializers import AuthorSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



# class AuthorView(APIView):
#     def get(self, request):
#         author = Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def author_list(request):
#     if request.method == 'GET':
#         author = Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data)
