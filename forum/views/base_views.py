from django.shortcuts import render, get_object_or_404, redirect
# get_object_or_404 주소 잘못입력했을 경우 404 페이지 출력을 위해 추가함
# 답변을 생성한 후 상세 화면을 호출하려면 redirect 함수를 사용. redirect 함수는 함수에 전달된 값을 참고하여 페이지 이동을 수행

# 페이징 기능을 위해 추가하는 클래스 - Paginator
from django.core.paginator import Paginator

# views 디렉터리에 파일이 위치하므로 ..models
from ..models import Question
# 목록 정렬을 위해 Count 추가
from django.db.models import Q, Count


# - index 함수의 매개변수 request 는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
# - request 는 사용자가 전달한 데이터를 확인할 때 사용된다.
def index(request):
    """
    forum 목록
    """

    # 입력 파라미터 - 페이지, 검색어
    # GET 방식 요청 URL에서 page값을 가져올 때 사용 ex. localhost:8000/forum/?page=1
    # page = request.GET.get('page', '1')
    # 페이지
    page = request.GET.get('page', '1')
    # 검색어
    kw = request.GET.get('kw', '')

    # Question 모델을 임포트해 Question 모델 데이터를 작성한 날짜의 역순으로 조회하기 위해 order_by 함수사용

    # question_list = Question.objects.order_by('-create_date')
    # 정렬기준
    so = request.GET.get('so', 'recent')
    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        # 최신순 정렬
        # '-create_date'는 - 기호가 앞에 붙어 있으므로 작성일시의 역순을 의미
        question_list = Question.objects.order_by('-create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            # 제목
            Q(subject__icontains=kw) |
            # 내용
            Q(content__icontains=kw) |
            # 질문 글쓴이
            Q(author__username__icontains=kw) |
            # 답변 글쓴이
            Q(answer__author__username__icontains=kw)
        ).distinct()

    # 페이징 처리 - 페이지당 10개씩
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    # page, kw, so 추가 - 입력받은 값을 searchForm 에 전달하기 위해
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}

    # # render 함수가 템플릿을 HTML로 변환하는 과정에서 사용되는 데이터
    # context = {'question_list': question_list}

    # render 함수는 context에 있는 Question 모델 데이터 question_list를 forum/question_list.html 파일에
    # 적용하여 HTML 코드로 변환한다. 장고에서는 이런 파일(forum/question_list.html)을 템플릿이라 한다.
    return render(request, 'forum/question_list.html', context)
    # return HttpResponse("안녕. 게시판 방문을 환영해.")


def detail(request, question_id):
    """
    forum 내용
    """
    # question_id 가 URL 매핑에 있던 question_id이다.
    # 즉, /forum/1/ 페이지가 호출되면 최종으로 detail 함수의 매개변수 question_id에 1이 전달
    # question = Question.objects.get(id=question_id)

    # get_object_or_404 함수는 모델의 기본키를 이용하여 모델 객체 한 건을 반환한다.
    # pk에 해당하는 건이 없으면 오류 대신 404 페이지를 반환
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'forum/question_detail.html', context)