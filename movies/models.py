from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    cin = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.username

class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()  # Durée en minutes
    abonnement = models.ForeignKey('Abonnement', on_delete=models.CASCADE, related_name='films', null=True, blank=True)
    image = models.ImageField(upload_to='film_images/', null=True, blank=True)  # Champ pour l'image
    link = models.URLField(max_length=200, null=True, blank=True)  # Champ pour le lien de redirection

    def __str__(self):
        return self.title

class Abonnement(models.Model):
    PLAN_CHOICES = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abonnements')
    plan_name = models.CharField(max_length=50, choices=PLAN_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_months = models.IntegerField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.plan_name} - {self.user.username}"
