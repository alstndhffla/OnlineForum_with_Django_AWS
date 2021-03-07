"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# include 함수를 임포트해 forum/의 URL 매핑을
# path('forum/', views.index)에서 path('forum/', include('forum.urls'))로 수정
from forum.views import base_views

# 장고가 사용자의 페이지 요청을 이해할 수 있도록 config/urls.py 파일을 수정
# 이를 'URL 매핑을 추가한다' 고 말함
# config/urls.py 파일은 페이지 요청 시 가장 먼저 호출되며, 요청 URL 과 뷰 함수를 1:1로 연결해준다.

"""
URL 은 웹 브라우저에 입력한 localhost:8000/forum 에서 호스트명 localhost 와 포트 번호 :8000이 생략된 
forum/ 이다. 호스트명과 포트는 장고가 실행되는 환경에 따라 변하는 값이며 장고가 이미 알고 있는 값이다. 
그러므로 urlpatterns 에는 호스트명과 포트를 입력하지 않는다.

config/urls.py 파일을 수정했음에도 
cmd 창에 AttributeError: module 'forum.views' has no attribute 'index' 
이런 오류가 발생한 이유는 URL 매핑에 추가한 뷰 함수인 views.index가 없기 때문
-> forum/views_copy.py 파일에 index 함수를 추가하자.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # forum/로 시작되는 페이지 요청은 모두 forum/urls.py 파일에 있는 URL 매핑을 참고하여 처리하라는 의미
    # -> forum 앱과 관련된 URL 요청은 앞으로 forum/urls.py 파일에서 관리하라는 뜻
    path('forum/', include('forum.urls')),
    # common 앱의 urls.py 파일을 사용하기 위해 -> /common/ 으로 시작하는 URL 은 common/urls.py 파일을 참조
    path('common/', include('common.urls')),

    # 로그인 성공시 '/' 에 해당되는 path
    # settings.py 의 LOGIN_REDIRECT_URL
    path('', base_views.index, name='index'),
]

# 서버 환경의 404 오류 페이지(404 오류 발생 시), page_not_found 함수가 호출되도록 함.
handler404 = 'common.views.page_not_found'
