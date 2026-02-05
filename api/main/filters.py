from django_filters import FilterSet, CharFilter, NumberFilter
from main.models import Service, Master, Gallery, Review


class ServiceFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['name',]


class MasterFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    position = CharFilter(field_name='position', lookup_expr='iexact')
    experience = CharFilter(field_name='experience', lookup_expr='icontains')
    service = CharFilter(field_name='service', lookup_expr='icontains')

    class Meta:
        model = Master
        fields = ['name', 'position', 'experience', 'service',]
        
    
class GalleryFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    service = CharFilter(field_name='service__name', lookup_expr='icontains')

    class Meta:
        model = Gallery
        fields = ['name', 'service']


class ReviewFilter(FilterSet):
    master = CharFilter(field_name='master', lookup_expr='icontains')
    rating = NumberFilter(field_name='score', lookup_expr='iexact')

    class Meta:
        model = Review
        fields = ['master', 'rating',]