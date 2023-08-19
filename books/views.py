from django.shortcuts import render
from rest_framework.views import APIView
from .permissions import ReadOnlyPermissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import ReadOnlyPermissions

# Create your views here.
# class BookLisApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookLisApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user=self.request.user
        return Book.objects.filter(user=user)




class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (ReadOnlyPermissions,)

# class BookDetailApiView(APIView):
#     def get(self,request,pk):
#         try:
#             books=Book.objects.get(id=pk)
#             serializer=BookSerializer(books)
#         except Book.DoesNotExist:
#             return Response({"msg":"Not found"})
#         return Response(serializer.data)
class BookCreateApiView(APIView):
     def post(self,request):
         book = request.data
         serializer=BookSerializer(data=book)
         if serializer.is_valid():
             serializer.save()
             return Response({"msg":"created"})


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def patch(self,request,pk):
        try:
            books=Book.objects.get(id=pk)
            data=request.data
            serializer=BookSerializer(instance=books,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
        except Book.DoesNotExist:
            return Response({"msg":"NOT FOUND"})
        return Response({"msg":f"{serializer.data} Updated"})


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self,request,pk):
        try:
            books=Book.objects.get(id=pk)
            books.delete()
        except Book.DoesNotExist:
            return Response({"msg":"NOT FOUND"})
        return Response({"msg":"DELETED"})



# @api_view(["GET"])
# def book_list_view(request,*args,**kwargs):
#     books=Book.objects.all()
#     serializer=BookSerializer(books,many=True)
#     return Response(serializer.data)
