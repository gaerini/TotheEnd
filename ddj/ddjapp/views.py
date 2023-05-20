from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        exist_user = User.objects.filter(username=username)

        if exist_user:
            error = "이미 존재하는 유저입니다."
            return render(request, 'registration/signup.html', {'error': error})
        
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        
        return redirect('home')
    
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
            return redirect(request.GET.get('next', '/'))

        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, 'registration/login.html', {'error': error})
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

