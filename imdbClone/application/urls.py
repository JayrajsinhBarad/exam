from django.urls import path
from application.views import *

urlpatterns = [
    path('', home, name='home1'),
    path('register/', register, name='register1'),
    path('login/', login, name='login1'),
    path('logout/', logout, name='logout1'),
    path('add-genres/', addGenre, name='addGenre1'),
    path('add-movie/', addMovie, name='addMovie1')  , 
]
