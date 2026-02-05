from .class_api import ServiceTypeViewSet, ServiceViewSet, MasterViewSet, GalleryViewSet, ReviewViewSet, AppointmentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'service_types', ServiceTypeViewSet, basename='service_types')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'masters', MasterViewSet, basename='masters')
router.register(r'gallery', GalleryViewSet, basename='gallery')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'appointments', AppointmentViewSet, basename='applications')


urlpatterns = [
    path('', include(router.urls)),
]