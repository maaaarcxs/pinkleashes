from rest_framework.generics import (GenericAPIView, CreateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from .serializers import (RegisterSerializer,
                          LoginSerializer,)
from rest_framework.response import Response
from django.conf import settings


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)