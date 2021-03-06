from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views

"""
코드 내용은 기존 config/urls.py 파일과 다르지 않다.
다만 path('', views.index) 입력 부분만 다르다. config/urls.py 파일에서 forum/에 대한 처리를 한 상태에서
forum/urls.py 파일이 실행되므로 첫 번째 매개변수에 forum/가 아닌 빈 문자열('')을 인자로 넘겨준 것

path('<int:question_id>/', views.detail),
질문 게시판을 클릭시 http://localhost:8000/forum/1/ 이렇게 변경되는데 이는 Question 모델 데이터 중 id값이 1인 데이터를 조회하라이다.
question_id 에 1 이라는 값이 저장되고 views.detail 함수가 실행된다.
int:는 question_id에 숫자가 매핑되었음을 의미
장고는 forum/까지는 config/urls.py의 URL 매핑을, 그 뒤 /1 은 forum/urls.py 의 매핑을 참고할 것이다.
매핑을 완료했으면 forum/views_copy.py 에서 화면을 추가해줘야한다.
"""

# 네임스페이스 추가(향후 forum 기능(앱)뿐이 아니라 추가 앱들이 있을 때 같은 URL 별칭 사용을 피하도록)
# 여기서 추가했으면 템플릿에서도 추가해줘야 한다. question_list.html 파일에
# <li><a href="{% url 'forum:detail' question.id %}">{{ question.subject }}</a></li> 이렇게.
app_name = 'forum'

urlpatterns = [

    # base_views.py
    # URL 하드코딩의 한계를 없애기 위해 name 을 사용해 별칭을 붙인다.
    # 이렇게 하면 주소 /forum/은 index라는 URL 별칭, /forum/2/는 detail이라는 URL 별칭이 생긴다.
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # answer_views.py
    # form 엘리먼트의 action 속성에 있는 {% url 'forum:answer_create' question.id %}에
    # 해당하는 URL 매핑이 없기 때문에 아래와 같이 등록해야함.
    # 상세 화면에서 <질문답변> 버튼을 눌렀을 때 작동할 form 엘리먼트의 /forum/answer/create/2/에 대한 URL 매핑을 추가한 것
    # 답변, 수정, 삭제 매핑 추가
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # question_views.py
    # 질문등록하기, 질문수정버튼, 질문 삭제 매핑 추가
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),


    # 댓글 매핑(등록, 수정, 삭제)
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),

    # 답변 댓글 매핑 - 댓글 등록은 답변 id, 댓글수정/삭제 는 댓글 id
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

    # 질문, 답변 추천 기능 매핑
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]
