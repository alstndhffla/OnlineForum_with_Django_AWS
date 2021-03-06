from django import template

# 마크다운 사용을 위한 2가지 임포트
import markdown  # 모듈
from django.utils.safestring import mark_safe   # 함수


"""
1. 템플릿 필터 작성 스크립트
페이지별로 항상 1로 시작하게 되는 게시물 번호를 해결하기 위함.
게시물 일련번호 = 전체 게시물 개수 - 시작 인덱스 - 현재 인덱스 + 1

2. 마크다운 필터 등록 (마크다운 확장 기능 문서: python-markdown.github.io/extensions/)
마크다운으로 작성한 문서를 HTML 문서로 변환하기 위함
markdown 모듈에 "nl2br", "fenced_code" 확장 도구를 설정 -> "nl2br"은 줄바꿈 문자를 <br> 태그로 바꿔 엔터를
한번만 눌러도 줄바끔을 가능케한다.

"""
register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))