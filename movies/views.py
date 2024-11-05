# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User, Film, Abonnement
from .serializers import UserSerializer, FilmSerializer, AbonnementSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_data = {
                "username": user.username,
                "role": user.role,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "address": user.address,
                "cin": user.cin,
                "phone": user.phone,
                "email": user.email,
            }
            return Response({
                "message": "Login successful",
                "user": user_data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "dashboard": "admin" if user.role == "admin" else "user"
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'admin':
            return Response({"message": "Welcome to the admin dashboard"}, status=status.HTTP_200_OK)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'user':
            return Response({"message": "Welcome to the user dashboard"}, status=status.HTTP_200_OK)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

# Ajout de films
class FilmCreateView(generics.CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

# Suppression de films
class FilmDeleteView(generics.DestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

class AbonnementListView(generics.ListAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    permission_classes = [IsAuthenticated]


class AbonnementCreateView(generics.CreateAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associer l'abonnement à l'utilisateur connecté
        serializer.save(user=self.request.user)