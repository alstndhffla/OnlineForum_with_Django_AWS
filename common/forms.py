from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
회원가입에 사용할 폼
"""

# django.contrib.auth.forms 패키지의 UserCreationForm 클래스를 상속
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

