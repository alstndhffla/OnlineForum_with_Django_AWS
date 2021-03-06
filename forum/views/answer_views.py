# 질문수정 함수를 추가하기 위해
from django.contrib import messages
# 로그인이 필요한 함수들에 대해 @login_required 적용을 위해 추가
# 로그인이 되었는지를 우선 검사 -> 로그아웃 상태에서 @login_required 애너테이션이 적용된 함수가 호출되면 자동으로 로그인 화면으로 이동할 것
from django.contrib.auth.decorators import login_required
# get_object_or_404 주소 잘못입력했을 경우 404 페이지 출력을 위해 추가함
# 답변을 생성한 후 상세 화면을 호출하려면 redirect 함수를 사용. redirect 함수는 함수에 전달된 값을 참고하여 페이지 이동을 수행
from django.shortcuts import render, get_object_or_404, redirect, redirect, resolve_url
# 앵커엘리먼트로 이동하도록 redirect 추가

from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer


# form 엘리먼트에 입력된 값을 받아 데이터베이스에 저장할 수 있도록 answer_create 함수
@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    forum 답변등록
    /forum/answer/create/2가 요청되면 question_id에는 2가 넘어온다.
    request 매개변수에는 forum/question_detail.html에서 textarea에 입력된 데이터가 담겨 넘어온다.
    이 값을 추출하기 위한 코드가 바로 request.POST.get('content')이다.
    그리고 Question 모델을 통해 Answer 모델 데이터를 생성하기 위해 question.answer_set.create를 사용
    """
    question = get_object_or_404(Question, pk=question_id)
    # # request.POST.get('content')는 POST 형식으로 전송된 form 데이터 항목 중 name이 content인 값을 의미
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            # 답변에 글쓴이 추가 - 모델에 추가한 author 적용 -> 로그인한 아이디의 User 모델 객체
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # 답변 등록시 앵커 앨리먼트로 이동하도록.
            return redirect('{}#answer_{}'.format(
                resolve_url('forum:detail', question_id=question.id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'forum/question_detail.html', context)

    # # 첫 번째 인수에는 이동할 페이지의 별칭을, 두 번째 인수에는 해당 URL 에 전달해야 하는 값을 입력
    # return redirect('forum:detail', question_id=question.id)


# 답변 수정 함수
@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    forum 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('forum:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            # 답변 수정시 앵커 앨리먼트로 이동하도록.
            return redirect('{}#answer_{}'.format(
                resolve_url('forum:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'forum/answer_form.html', context)


# 답변 삭제 함수
@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    forum 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('forum:detail', question_id=answer.question.id)