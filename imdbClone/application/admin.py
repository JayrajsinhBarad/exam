from django.contrib import admin
from application.models import *

class genreRegister(admin.ModelAdmin):
    list_display = ['movieGenre', 'genreInfo']
admin.site.register(Genre, genreRegister)

class userRegister(admin.ModelAdmin):
    list_display = ['userName', 'userEmail', 'userPhone']
admin.site.register(UserRegister, userRegister)

class movieRegister(admin.ModelAdmin):
    list_display = ['movieName', 'movieDescription']
admin.site.register(Movie, movieRegister)