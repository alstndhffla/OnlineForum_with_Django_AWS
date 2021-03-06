"""
코드가 너무 길어서
유지보수가 용이하게 views 폴더를 만들어 분리했다.
이 파일 사용x
views 폴더에 __init__.py 를 생성하고 urls.py 파일을 수정해도 된다.
"""


# from django.shortcuts import render, get_object_or_404, redirect
# # get_object_or_404 주소 잘못입력했을 경우 404 페이지 출력을 위해 추가함
# # 답변을 생성한 후 상세 화면을 호출하려면 redirect 함수를 사용. redirect 함수는 함수에 전달된 값을 참고하여 페이지 이동을 수행
# from .models import Question, Answer, Comment
#
# # Create your views here.
#
# from django.http import HttpResponse
# from django.utils import timezone
# # 질문등록기능, 답변등록기능 추가를 위한 import
# from .forms import QuestionForm, AnswerForm, CommentForm
# # 페이징 기능을 위해 추가하는 클래스 - Paginator
# from django.core.paginator import Paginator
# # 로그인이 필요한 함수들에 대해 @login_required 적용을 위해 추가
# # 로그인이 되었는지를 우선 검사 -> 로그아웃 상태에서 @login_required 애너테이션이 적용된 함수가 호출되면 자동으로 로그인 화면으로 이동할 것
# from django.contrib.auth.decorators import login_required
# # 질문수정 함수를 추가하기 위해
# from django.contrib import messages
#
#
# # - index 함수의 매개변수 request 는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
# # - request 는 사용자가 전달한 데이터를 확인할 때 사용된다.
# def index(request):
#     """
#     forum 목록
#     """
#
#     # 입력 파라미터 - 페이지
#     # GET 방식 요청 URL에서 page값을 가져올 때 사용 ex. localhost:8000/forum/?page=1
#     page = request.GET.get('page', '1')
#
#     # Question 모델을 임포트해 Question 모델 데이터를 작성한 날짜의 역순으로 조회하기 위해 order_by 함수사용
#     # '-create_date'는 - 기호가 앞에 붙어 있으므로 작성일시의 역순을 의미
#     question_list = Question.objects.order_by('-create_date')
#
#     # 페이징 처리 - 페이지당 10개씩
#     paginator = Paginator(question_list, 10)
#     page_obj = paginator.get_page(page)
#
#     context = {'question_list': page_obj}
#
#     # # render 함수가 템플릿을 HTML로 변환하는 과정에서 사용되는 데이터
#     # context = {'question_list': question_list}
#
#     # render 함수는 context에 있는 Question 모델 데이터 question_list를 forum/question_list.html 파일에
#     # 적용하여 HTML 코드로 변환한다. 장고에서는 이런 파일(forum/question_list.html)을 템플릿이라 한다.
#     return render(request, 'forum\question_list.html', context)
#     return HttpResponse("안녕. 질의응답 게시판 방문을 환영해.")
#
#
# def detail(request, question_id):
#     """
#     forum 내용
#     """
#     # question_id 가 URL 매핑에 있던 question_id이다.
#     # 즉, /forum/1/ 페이지가 호출되면 최종으로 detail 함수의 매개변수 question_id에 1이 전달
#     # question = Question.objects.get(id=question_id)
#
#     # get_object_or_404 함수는 모델의 기본키를 이용하여 모델 객체 한 건을 반환한다.
#     # pk에 해당하는 건이 없으면 오류 대신 404 페이지를 반환
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'forum/question_detail.html', context)
#
#
# # form 엘리먼트에 입력된 값을 받아 데이터베이스에 저장할 수 있도록 answer_create 함수
# @login_required(login_url='common:login')
# def answer_create(request, question_id):
#     """
#     forum 답변등록
#     /forum/answer/create/2가 요청되면 question_id에는 2가 넘어온다.
#     request 매개변수에는 forum/question_detail.html에서 textarea에 입력된 데이터가 담겨 넘어온다.
#     이 값을 추출하기 위한 코드가 바로 request.POST.get('content')이다.
#     그리고 Question 모델을 통해 Answer 모델 데이터를 생성하기 위해 question.answer_set.create를 사용
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     # # request.POST.get('content')는 POST 형식으로 전송된 form 데이터 항목 중 name이 content인 값을 의미
#     # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             # 답변에 글쓴이 추가 - 모델에 추가한 author 적용 -> 로그인한 아이디의 User 모델 객체
#             answer.author = request.user
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('forum:detail', question_id=question.id)
#     else:
#         form = AnswerForm()
#     context = {'question': question, 'form': form}
#     return render(request, 'forum/question_detail.html', context)
#
#     # # 첫 번째 인수에는 이동할 페이지의 별칭을, 두 번째 인수에는 해당 URL 에 전달해야 하는 값을 입력
#     # return redirect('forum:detail', question_id=question.id)
#
#
# # 질문등록 URL 매핑에 의해 실행될 views.question_create 함수
# @login_required(login_url='common:login')
# def question_create(request):
#     """
#     forum 질문등록
#     question/create/가 GET 방식으로 요청되어 질문 등록 화면이 나타나고,
#     질문 등록 화면에서 입력값을 채우고 <저장하기> 버튼을 누르면
#     question/create/가 POST 방식으로 요청되어 데이터가 저장된다.
#
#     GET 방식의 경우 QuestionForm()과 같이 입력값 없이 객체를 생성했고
#     POST 방식의 경우에는 QuestionForm(request.POST)처럼 화면에서 전달받은 데이터로 폼의 값이 채워지도록 객체를 생성
#
#     """
#     if request.method == 'POST':
#         # QuestionForm 클래스는 질문을 등록하기 위해 사용하는 장고의 폼
#         form = QuestionForm(request.POST)
#         # form.is_valid 함수는 POST 요청으로 받은 form이 유효한지 검사. 유효하지 않으면 폼에 오류가 저장되어 전달됨
#         if form.is_valid():
#             # form으로 Question 모델 데이터를 저장하기 위한 코드. commit=False 은 임시저장을 의미
#             question = form.save(commit=False)
#             # 질문에 글쓴이 추가
#             question.author = request.user
#             question.create_date = timezone.now()
#             question.save()
#             return redirect('forum:index')
#     else:
#         form = QuestionForm()
#
#     context = {'form': form}
#     return render(request, 'forum/question_form.html', context)
#
#
# @login_required(login_url='common:login')
# def question_modify(request, question_id):
#     """
#     forum 질문수정
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('forum:detail', question_id=question.id)
#
#     if request.method == "POST":
#         # 질문수정을 위한 값 덮어쓰기
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             # 질문 수정일시를 저장
#             question.modify_date = timezone.now()
#             question.save()
#             return redirect('forum:detail', question_id=question.id)
#     else:
#         # 질문수정화면에서 기존 제목과 내용을 반영함.
#         form = QuestionForm(instance=question)
#     context = {'form': form}
#     return render(request, 'forum/question_form.html', context)
#
#
# # 질문삭제 함수
# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     """
#     forum 질문삭제
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('forum:detail', question_id=question.id)
#     question.delete()
#     return redirect('forum:index')
#
#
# # 답변 수정 함수
# @login_required(login_url='common:login')
# def answer_modify(request, answer_id):
#     """
#     forum 답변수정
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('forum:detail', question_id=answer.question.id)
#
#     if request.method == "POST":
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('forum:detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'forum/answer_form.html', context)
#
#
# # 답변 삭제 함수
# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     """
#     forum 답변삭제
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         answer.delete()
#     return redirect('forum:detail', question_id=answer.question.id)
#
#
# @login_required(login_url='common:login')
# def comment_create_question(request, question_id):
#     """
#     forum 질문댓글등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.question = question
#             comment.save()
#             return redirect('forum:detail', question_id=question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, 'forum/comment_form.html', context)
#
#
# # get 방식이면 기존 댓글 조회해 폼 반영.
# # post 방식이면 입력된 값으로 수정
# @login_required(login_url='common:login')
# def comment_modify_question(request, comment_id):
#     """
#     forum 질문댓글수정
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글수정권한이 없습니다')
#         return redirect('forum:detail', question_id=comment.question.id)
#
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.modify_date = timezone.now()
#             comment.save()
#             return redirect('forum:detail', question_id=comment.question.id)
#     else:
#         form = CommentForm(instance=comment)
#     context = {'form': form}
#     return render(request, 'forum/comment_form.html', context)
#
#
# @login_required(login_url='common:login')
# def comment_delete_question(request, comment_id):
#     """
#     forum 질문댓글삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없습니다')
#         return redirect('forum:detail', question_id=comment.question.id)
#     else:
#         comment.delete()
#     return redirect('forum:detail', question_id=comment.question.id)
#
#
# @login_required(login_url='common:login')
# def comment_create_answer(request, answer_id):
#     """
#     forum 답글댓글등록
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.answer = answer
#             comment.save()
#             return redirect('forum:detail', question_id=comment.answer.question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, 'forum/comment_form.html', context)
#
#
# @login_required(login_url='common:login')
# def comment_modify_answer(request, comment_id):
#     """
#     forum 답글댓글수정
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글수정권한이 없습니다')
#         return redirect('forum:detail', question_id=comment.answer.question.id)
#
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.modify_date = timezone.now()
#             comment.save()
#             return redirect('forum:detail', question_id=comment.answer.question.id)
#     else:
#         form = CommentForm(instance=comment)
#     context = {'form': form}
#     return render(request, 'forum/comment_form.html', context)
#
#
# @login_required(login_url='common:login')
# def comment_delete_answer(request, comment_id):
#     """
#     forum 답글댓글삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없습니다')
#         return redirect('forum:detail', question_id=comment.answer.question.id)
#     else:
#         comment.delete()
#     return redirect('forum:detail', question_id=comment.answer.question.id)
#














