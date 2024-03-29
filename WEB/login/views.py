from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from login.forms import UserForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.cache import never_cache

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'login/signup.html', {'form': form})

def agree(request):
    return render(request, 'login/agree.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            return redirect('file_upload_app:file_upload')
        else:
            return render(request, "login/login.html", {
                'error': '아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다.',
                'error2' : '입력하신 내용을 다시 확인해주세요.',
            })
    else:
        return render(request, "login/login.html")

@never_cache  
def logout(request):
    if request.method == 'POST':
        request.session.flush()  # 세션 삭제 추가
        response = redirect('/')
        return response
    else:
        return render(request, 'main.html')

def use_acc(request):
    return render(request, 'login/use_acc.html')

