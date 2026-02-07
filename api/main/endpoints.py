from .class_api import ServiceTypeApiViewSet, ServiceApiViewSet, MasterApiViewSet, GalleryApiViewSet, ReviewApiViewSet, AppointmentApiViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'service_types', ServiceTypeApiViewSet, basename='service_types')
router.register(r'services', ServiceApiViewSet, basename='services')
router.register(r'masters', MasterApiViewSet, basename='masters')
router.register(r'gallery', GalleryApiViewSet, basename='gallery')
router.register(r'reviews', ReviewApiViewSet, basename='reviews')
router.register(r'appointments', AppointmentApiViewSet, basename='applications')


urlpatterns = [
    path('', include(router.urls)),
]