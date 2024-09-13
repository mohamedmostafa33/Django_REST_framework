from rest_framework import viewsets
from .models import Book, Magazine
from .serializers import BookSerializer ,MagazineSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter, MagazineFilter

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter

class MagazineViewSet(viewsets.ModelViewSet):
    serializer_class = MagazineSerializer
    queryset = Magazine.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MagazineFilter

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view.'})