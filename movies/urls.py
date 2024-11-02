# movies/urls.py
from django.urls import path
from .views import RegisterView, LoginView, FilmListView, UserDashboardView, AdminDashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('films/', FilmListView.as_view(), name='film-list'),
    path('dashboard/user/', UserDashboardView.as_view(), name='user-dashboard'),
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
]
