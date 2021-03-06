# 질문수정 함수를 추가하기 위해
from django.contrib import messages

# 로그인이 필요한 함수들에 대해 @login_required 적용을 위해 추가
# 로그인이 되었는지를 우선 검사 -> 로그아웃 상태에서 @login_required 애너테이션이 적용된 함수가 호출되면 자동으로 로그인 화면으로 이동할 것
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
# get_object_or_404 주소 잘못입력했을 경우 404 페이지 출력을 위해 추가함
# 답변을 생성한 후 상세 화면을 호출하려면 redirect 함수를 사용. redirect 함수는 함수에 전달된 값을 참고하여 페이지 이동을 수행

from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


# 질문등록 URL 매핑에 의해 실행될 views.question_create 함수
@login_required(login_url='common:login')
def question_create(request):
    """
    forum 질문등록
    question/create/가 GET 방식으로 요청되어 질문 등록 화면이 나타나고,
    질문 등록 화면에서 입력값을 채우고 <저장하기> 버튼을 누르면
    question/create/가 POST 방식으로 요청되어 데이터가 저장된다.

    GET 방식의 경우 QuestionForm()과 같이 입력값 없이 객체를 생성했고
    POST 방식의 경우에는 QuestionForm(request.POST)처럼 화면에서 전달받은 데이터로 폼의 값이 채워지도록 객체를 생성

    """
    if request.method == 'POST':
        # QuestionForm 클래스는 질문을 등록하기 위해 사용하는 장고의 폼
        form = QuestionForm(request.POST)
        # form.is_valid 함수는 POST 요청으로 받은 form이 유효한지 검사. 유효하지 않으면 폼에 오류가 저장되어 전달됨
        if form.is_valid():
            # form으로 Question 모델 데이터를 저장하기 위한 코드. commit=False 은 임시저장을 의미
            question = form.save(commit=False)
            # 질문에 글쓴이 추가
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('forum:index')
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'forum/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    forum 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('forum:detail', question_id=question.id)

    if request.method == "POST":
        # 질문수정을 위한 값 덮어쓰기
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            # 질문 수정일시를 저장
            question.modify_date = timezone.now()
            question.save()
            return redirect('forum:detail', question_id=question.id)
    else:
        # 질문수정화면에서 기존 제목과 내용을 반영함.
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'forum/question_form.html', context)


# 질문삭제 함수
@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    forum 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('forum:detail', question_id=question.id)
    question.delete()
    return redirect('forum:index')
