import django_filters
from .models import Book, Magazine

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author']

class MagazineFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    publisher = django_filters.CharFilter(lookup_expr='icontains')
    issue_number = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Magazine
        fields = ['title', 'publisher', 'issue_number']
