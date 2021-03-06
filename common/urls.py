from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
"""
/common/으로 시작하는 URL은 모두 common/urls.py 파일을 참조

로그인 기능은 django.contrib.auth 앱을 사용할 것. 그래서 common/views_copy.py 파일은 수정할 필요x. 
-> django.contrib.auth 앱의 LoginView 클래스를 사용


"""
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    # 로그아웃 - {% url 'common:logout' %} 에 해당하는 매핑
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 회원가입 URL 매핑 - login.html 파일의 {% url 'common:signup' %}
    path('signup/', views.signup, name='signup'),
]