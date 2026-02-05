from django.urls import path, include


urlpatterns = [
    path('', include('api.yasg')),
    path('main/', include('api.main.endpoints')),
    path('auth/', include('api.auth.endpoints'))
]