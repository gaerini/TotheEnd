from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Room, Request, Chatting, Comment, Recomment
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        stone_id = request.POST['stone_id']
        print(stone_id, "stone_id")
        return redirect('stoneDetail', stone_id)
    stones = Room.objects.all()
    return render(request, 'home.html', {'stones':stones})

def stoneDetail(request, room_id):
    room = Room.objects.get(pk = room_id)
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'send':
            return redirect('stoneRequest', room_id)

    return render(request, 'stoneDetail.html', {'room': room})


# def myStone(request, room_id):


def stoneRequest(request, room_id):
    if request.method == 'POST':
        member = request.POST.get('member')
        talk_topic = request.POST.get('talk_topic')
        age = request.POST.get('age')
        sex = request.POST.get('sex')

        room = Room.objects.get(id=room_id)
        sender = request.user
        if room.matched == 0:
            Request.objects.create(
                sender=sender, 
                receiver=room, 
                member=member, 
                talk_topic=talk_topic, 
                age=age, 
                sex=sex
                )
            Room.objects.filter(id=room_id).update(
                    matched = 1
                )
        else :
            return redirect('stone') # 여기에 오류 메세지, 이미 matched 됐다

            
        
        return redirect('home')  # 홈페이지로 리다이렉트 혹은 메시지를 보여줄 수 있음

    return render(request, 'stoneRequest.html')



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
    article=Chatting.objects.get(pk=article_id)
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


def confirm(request, room_id):
    stoneRequest=Request.objects.get(receiver__id=room_id)
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'reject':
            Room.objects.filter(id=room_id).update(
                matched = 0
            )
        elif action == 'accept':    
            Room.objects.filter(id=room_id).update(
                matched = 2
            )

        return redirect('home')
    
    return render(request, 'confirm.html', {'stoneRequest':stoneRequest})

        
      
def stone(request):
    if request.method=="POST":
        Room.objects.create(
            user = request.user,
            current_member=request.POST['current_member'],
            want_member=request.POST['want_member'],
            talk_topic=request.POST['talk_topic'],
            age=request.POST['age'],
            give_food = request.POST['give_food'],
            sex = request.POST['sex'],
            matched = 0,
        )
        return redirect('home')
    
    return render(request, 'stackStone.html')

    
