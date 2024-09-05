from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from serializers.serializer_users import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
        
class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página de productos
            return redirect('ruta_a_productos')  # Cambia a tu ruta real
        else:
            return Response({"error": "Invalid credentials"}, status=400)
