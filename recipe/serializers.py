from django.contrib.auth import get_user_model

from .models import Recipe, Ingredient, Comentarie, Rating
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'profile']

    def create(self, validated_data):
        # Извлечение данных профиля
        profile_data = validated_data.pop('profile')
        # Создание пользователя
        user = User.objects.create(**validated_data)
        # Создание профиля, связанного с пользователем
        Profile.objects.create(user=user, **profile_data)
        return user


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class ComentarieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarie
        fields = ['cvyaz','name']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields ='__all__'