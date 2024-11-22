from cProfile import Profile
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    photo = models.ImageField(upload_to='media')


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)


class Comentarie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cvyaz = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    name = models.TextField()


    def __str__(self):
        return self.user.username

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ramka = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])


