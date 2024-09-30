from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['put'], detail=True)
    def update_book(self, request, pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(methods=['patch'], detail=True)
    def partial_update_book(self, request, pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)



    def index(request):
        books = Book.objects.all()
        return render(request, 'index.html', {'books':books})