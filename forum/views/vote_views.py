from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    forum 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        # ManyToManyField 는 중복허락 x
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        # ManyToManyField 를 사용했기 때문에 add 로 추천인 추가
        question.voter.add(request.user)
    return redirect('forum:detail', question_id=question.id)


@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    forum 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('forum:detail', question_id=answer.question.id)