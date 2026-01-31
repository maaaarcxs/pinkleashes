import django_filters
from django import forms
from . models import Service, Master, Review

class ServiceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Название услуги")

    class Meta:
        model = Service
        fields = ("title",)


class MasterFilter(django_filters.FilterSet):
    position = django_filters.ChoiceFilter(choices=Master.POSITIONS, widget=forms.Select, empty_label="Не выбрано", label="Позиция")
    experience = django_filters.NumberFilter(label="Стаж (лет)")

    class Meta:
        model = Master
        fields = ("position", "experience")


class ReviewFilter(django_filters.FilterSet):
    master = django_filters.ModelChoiceFilter(choice=Master.name, widget=forms.Select, empty_label="Мастеры", label="Выберите мастера")
    rating = django_filters.NumberFilter(label="Рейтинги")

    class Meta:
        model = Review
        fields = ("master", "rating")