from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import RecipeViewSet, ProfileCreateAPIView, ComentarieCreateAPIView, RatingCreateAPIView

router = DefaultRouter()
router.register(r'recipe', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('regis/',ProfileCreateAPIView.as_view()),
    path('comentarie/',ComentarieCreateAPIView.as_view()),
    path('rating/',RatingCreateAPIView.as_view())
]


