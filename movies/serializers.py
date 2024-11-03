from rest_framework import serializers
from .models import User, Film, Abonnement

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'role', 'first_name', 'last_name', 'address', 'cin', 'phone', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash le mot de passe
        user.save()
        return user

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'  # Inclure tous les champs de Film

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'  # Inclure tous les champs d'Abonnement
