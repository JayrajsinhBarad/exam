from django.db import models

class Genre(models.Model):
    movieGenre = models.CharField(max_length=25)
    genreInfo = models.CharField(max_length=200)

class UserRegister(models.Model):
    userName = models.CharField(max_length=30)
    userEmail = models.EmailField()
    userPhone = models.IntegerField()
    userAddress = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=15)

class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movieName = models.CharField(max_length=50)
    movieImage = models.ImageField(upload_to='product')
    movieDescription = models.TextField()