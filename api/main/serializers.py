from rest_framework import serializers
from django.conf import settings
from main.models import ServiceType, Service, Master, Gallery, Review, Appointment
from datetime import datetime
from django.utils import timezone


class ServiceTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

    
class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class MasterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError()
        return value


class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'