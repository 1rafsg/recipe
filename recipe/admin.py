from django.contrib import admin
from .models import Recipe, Rating
from .models import Profile
from .models import Ingredient
from .models import Comentarie

admin.site.register(Recipe)
admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(Comentarie)
admin.site.register(Rating)


# Register your models here.
