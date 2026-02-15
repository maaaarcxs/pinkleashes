from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from main.models import ServiceType, Service, Master, Gallery, Review, Appointment
from .serializers import ServiceTypeSerializers, ServiceSerializers, MasterSerializers, GallerySerializers, ReviewSerializers, AppointmentSerializers


class ServiceTypeApiViewSet(ReadOnlyModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializers
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny()]
    

class ServiceApiViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny()]
    

class MasterApiViewSet(ReadOnlyModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializers
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny()]
    

class GalleryApiViewSet(ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny()]
    

class ReviewApiViewSet(CreateModelMixin, GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticated]
    

class AppointmentApiViewSet(GenericViewSet, CreateModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    permission_classes = [IsAuthenticated]
