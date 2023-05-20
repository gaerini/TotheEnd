from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
<<<<<<< HEAD
from .models import Room, Request
=======
from .models import Article, Comment, Recomment


>>>>>>> 54e0f47e3f36fda8c0c33498f95dfde306650356
# Create your views here.
def home(request):
    stones = Room.objects.all()
    return render(request, 'home.html', {'stones':stones})

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

def detail(request, article_id):
    article=Article.objects.get(id=article_id)
    if request.method=="POST":
        Comment.objects.create(
            article=article,
            content=request.POST['content'],
        )
        return redirect('detail', article_id)
    return render(request, 'detail.html', {'article':article})
def delete(request, article_id):
    article=Article.objects.get(id=article_id).delete()
    return redirect('home')

def deleteComment(request, article_id, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect('detail', article_id)

def recomment(request, article_id, comment_id):
    comment=Comment.objects.get(id=comment_id)
    if request.method=="POST":
        Recomment.objects.create(
            comment=comment,
            content=request.POST['content'],
        )
        return redirect('detail', article_id)

def deleteRecomment(request, article_id, recomment_id):
    Recomment.objects.get(id=recomment_id).delete()
    return redirect('detail', article_id)