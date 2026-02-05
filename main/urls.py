from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name="homepage"),
    path('about_us/', views.AboutUsPageView.as_view(), name="about_us"),
    path('services_list/', views.ServiceView.as_view(), name="services_list"),
    path('masters_list/', views.MastersView.as_view(), name="masters_list"),
    path('master_details/', views.MasterDetailView.as_view(), name="master_details"),
    path('appointment_create/', views.AppointmentView.as_view(), name="appointment_create")
]
