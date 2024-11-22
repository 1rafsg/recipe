from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import RecipeSerializer, ComentarieSerializer, RatingSerializer
from .models import Recipe, Profile, Comentarie, Rating
from .serializers import UserSerializer
from rest_framework import permissions


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ComentarieCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comentarie.objects.all()
    serializer_class = ComentarieSerializer

    def perform_create(self, serializer):
        # Set the user as the author of the comment
        serializer.save(user=self.request.user)


class RatingCreateAPIView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes =[permissions.AllowAny]



