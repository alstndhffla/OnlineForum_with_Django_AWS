from django import forms
from forum.models import Question, Answer, Comment
# 질문 등록기능 추가 Question
# 담변 등록기능 추가 Answer

"""
forms.Form을 상속받으면 폼, forms.ModelForm을 상속받으면 모델 폼이라 부른다. 
모델 폼은 말 그대로 모델과 연결된 폼이며, 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있다
"""


# ModelForm을 상속받은 QuestionForm 클래스
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        # # 질문등록화면에는 {{ form.as_p }} 부트스트랩을 적용할 수 없다.
        # # 빠르게 템플릿을 만들 수는 있지만 HTML 코드가 자동으로 생성되어 특정 태크 추가나 클래스 추가에 제한이 생김.
        # # 무튼 그래서 속성을 추가함
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        # 질문등록 화면에 나오는 영어를 한글화
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }