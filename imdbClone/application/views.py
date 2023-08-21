from django.shortcuts import render, redirect
from application.models import *

def home(request):
    if 'email' in request.session:
        email = request.session['email']
        return render(request, 'home.html', {'email':email})
    else:
        return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        data = UserRegister(userName = name, userEmail = email, userPhone = phone, userAddress = address, userPassword = password)
        mail = UserRegister.objects.filter(userEmail = email)
        if len(mail) == 0:
            data.save()
            return redirect('login1')
        else:
            return render(request, 'register.html', {'message':'User already exist'})

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            data = UserRegister.objects.get(userEmail = email, userPassword = password)
            if data:
                request.session['email'] = data.userEmail
                request.session['id'] = data.pk
                return redirect('home1')
            else:
                return render(request, 'login.html', {'message':'Invalid email or password'})
        except:
            return render(request, 'login.html', {'message':'Invalid email or password'})
    return render(request, 'login.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['id']
        return redirect('home1')
    else:
        return redirect('home1')
    
def addGenre(request):
    if 'email' in request.session:
        if request.method == 'POST':
            genre = request.POST['genre']
            discription = request.POST['discription']
            data = Genre(movieGenre = genre, genreInfo = discription)
            category = Genre.objects.filter(movieGenre = genre)
            if len(category) == 0:
                data.save()
                return render(request, 'addGenre.html', {'message':"Genre added successfully."})
            else:
                return render(request, 'addGenre.html', {'message':'Genre already exist'})
        return render(request, 'addGenre.html')
    else:
        return redirect('login1')
    
def addMovie(request):
    if 'email' in request.session:
        return render(request, 'addMovie.html')
    else:
        return redirect('login1')