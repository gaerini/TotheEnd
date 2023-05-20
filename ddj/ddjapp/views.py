from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Room, Request, Article, Comment, Recomment
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        stone_id = request.POST['stone_id']
        print(stone_id, "stone_id")
        return redirect('stonedetail', stone_id)
    stones = Room.objects.all()
    return render(request, 'home.html', {'stones':stones})

def stonedetail(request, stone_id):
    stone = Room.objects.get(pk = stone_id)
    return render(request, 'StoneDetail.html', {'stone': stone})

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


def confirm(request):
    if request.method == 'POST' and request.is_ajax():
        # 매칭 완료 버튼이 눌렸을 때의 로직을 구현합니다.
        # 예시로 Room 모델을 가정하고 해당 모델의 matched 필드를 True로 변경하는 코드를 작성합니다.
        
        # 예시: Room 객체 가져오기
        room_id = request.POST.get('room_id')  # AJAX 요청에서 전달된 방(room)의 ID를 가져옵니다.
        room = Room.objects.get(id=room_id)  # 방 객체를 가져옵니다.

        # 매칭 완료 처리
        room.matched = True  # matched 필드 값을 True로 변경합니다.
        room.save()  # 변경사항을 저장합니다.

        # 변경된 값을 응답으로 반환합니다.
        response_data = {
            'success': True,
            'message': '매칭이 완료되었습니다.'
        }
        return JsonResponse(response_data)
      
def stone(request):
    if request.method=="POST":
        Room.objects.create(
            current_member=request.POST['current_member'],
            want_member=request.POST['want_member'],
            finished=False,
            talk_topic=request.POST['talk_topic'],
            age=request.POST['age'],
            give_food = request.POST['give_food'],
            sex = request.POST['sex'],
            request_member=False,
        )

    
