from django.db import models
from django.contrib.auth.models import User

"""
(모델 추가 후) 장고의 개발 패턴 순서 5가지.

1. 화면에 버튼 등 기능 추가하기
2. urls.py 파일에 기능에 해당하는 URL 매핑 추가하기
3. forms.py 파일에 폼 작성하기
4. views_copy.py 파일에 URL 매핑에 추가한 함수 작성하기
5. 함수에서 사용할 템플릿 작성하기

"""

# Create your models here.


class Question(models.Model):
    # 질문의 제목(최대 200자)
    subject = models.CharField(max_length=200)
    # 질문의 내용(글자 수 제한이 없는 데이터 - TextField)
    content = models.TextField()
    # 질문을 작성한 일시
    create_date = models.DateTimeField()
    # on_delete=models.CASCADE는 아이디가 삭제되면 아이디와 연결된 Question 모델 데이터를 모두 삭제
    # voter 를 추가하게 되면 User 모델을 같이 참조하게 되어 오류가 발샌한다. 그래서 related_name 옵션을 추가해줘야한다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # 질문수정일시 - 수정일시는 수정한 경우에만 생성되는 데이터 -> 어떤 조건으로든 값을 비워둘 수 있도록함.
    modify_date = models.DateTimeField(null=True, blank=True)
    # voter(좋아오 누르는 횟수를 위해) - 장고는 다대다 관계(ManyToManyField)를 지원한다.
    voter = models.ManyToManyField(User, related_name='voter_question')

    """
    Question.objects.all() 입력시 저장된 모든 데이터를 조회해주는데 결과를 보면 
    <Question object (1)>, <Question object (2)> 로 출력된다. 
    그리고 <Question object (1)>, <Question object (2)>의 1, 2가 바로 장고에서 Question 모델 데이터에 
    자동으로 입력해 준 id 값이란 걸 알 수 있다. 이때 아래와 같은 함수를 추가하면 데이터조회시 위에 있는 id 값이 아닌 제목을 표시해준다.
    """
    def __str__(self):
        return self.subject


class Answer(models.Model):
    # 질문(어떤 질문의 답변인지 알아야 하므로 질문 속성이 필요하다)
    # 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey를 이용
    # 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미
    """
    장고에서 사용할 수 있는 속성이 궁금하면
    장고 속성 공식 문서 주소: docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 답변 내용
    content = models.TextField()
    # 답변을 작성한 일시
    create_date = models.DateTimeField()
    # 답변 등록자
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    # 답변수정일지
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


# 댓글 사용 모델.
class Comment(models.Model):
    # 댓글쓴이
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 댓글 내용
    content = models.TextField()
    # 댓글 작성일시
    create_date = models.DateTimeField()
    # 댓글 수정일시
    modify_date = models.DateTimeField(null=True, blank=True)
    # 댓글이 달린 질문
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    # 댓글이 달린 답변
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
