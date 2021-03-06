from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


# Create your views here.


# 회원가입을 위한 signup 함수
def signup(request):
    """
    아이디 생성
    POST 요청인 경우 화면에서 입력한 데이터로 새로운 사용자를 생성, GET 요청인 경우 common/signup.html 화면을 반환
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


# 404 페이지 발생시 사용될 함수
def page_not_found(request, exception):
    # exception 매개변수는 오류의 내용을 담고 있는 것.
    """
    404 Page not found
    """
    # 오류발생시 띄워주는 common/404.html 템플릿 파일을 작성
    return render(request, 'common/404.html', {})
