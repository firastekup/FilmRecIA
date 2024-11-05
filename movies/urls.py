# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AbonnementDeleteView, RegisterView, LoginView, FilmListView, FilmCreateView, FilmDeleteView, UserDashboardView, AdminDashboardView, AbonnementListView, AbonnementCreateView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('films/', FilmListView.as_view(), name='film-list'),
    path('films/create/', FilmCreateView.as_view(), name='film-create'),
    path('films/<int:pk>/delete/', FilmDeleteView.as_view(), name='film-delete'),
    path('abonnements/', AbonnementListView.as_view(), name='abonnement-list'),
    path('abonnements/create/', AbonnementCreateView.as_view(), name='abonnement-create'),
      # Route pour créer un abonnement
    path('dashboard/user/', UserDashboardView.as_view(), name='user-dashboard'),
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('abonnements/<int:pk>/delete/', AbonnementDeleteView.as_view(), name='abonnement-delete'),
      path('users/', UserListView.as_view(), name='user-list'),
    # JWT token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
