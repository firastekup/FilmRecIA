from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User, Film, Abonnement
from .serializers import UserSerializer, FilmSerializer, AbonnementSerializer

# Vue d'enregistrement des utilisateurs
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Vue de connexion des utilisateurs
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

# Vue du tableau de bord administrateur
class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'admin':
            return Response({"message": "Welcome to the admin dashboard"}, status=status.HTTP_200_OK)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

# Vue du tableau de bord utilisateur
class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'user':
            return Response({"message": "Welcome to the user dashboard"}, status=status.HTTP_200_OK)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

# Vue pour lister les films
class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

# Vue pour ajouter des films
class FilmCreateView(generics.CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

# Vue pour supprimer des films
class FilmDeleteView(generics.DestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

# Vue pour lister les abonnements
class AbonnementListView(generics.ListAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    permission_classes = [IsAuthenticated]

# Vue pour créer un abonnement
class AbonnementCreateView(generics.CreateAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    permission_classes = [IsAuthenticated]  # Assurez-vous que seul un utilisateur authentifié peut créer un abonnement

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

# Vue pour supprimer un abonnement
class AbonnementDeleteView(generics.DestroyAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    permission_classes = [IsAuthenticated]


# views.py

from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.role == 'admin':
            return super().get(request, *args, **kwargs)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
