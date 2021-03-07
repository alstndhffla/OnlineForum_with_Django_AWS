from .base import *
"""
서버 환경 담당파일
"""


# AWS 서버 고정 ip 등록
ALLOWED_HOSTS = ['3.34.54.66']

"""
장고에 내장된 개발 서버는 장고 Admin이 사용될 때 자동으로
/home/ubuntu/venvs/mysite/lib/python3.6/site-packages/django/contrib/admin/static
여기서 정적파일을 읽고

Nginx는 /home/ubuntu/projects/mysite/static 여기서 정적파일을 읽는다.

그래서 http://3.34.54.66/admin 입력 후 보이는 브라우저는 스타일깨져서 나타남.

이를 해결하기 위해서는 장고 환경설정 파일에 STATIC_ROOT 디렉터리를 설정하고 
관리자 앱의 정적 파일을 STATIC_ROOT 디렉터리로 복사해야한다.
(python manage.py collectstatic 입력해 관리자 앱의 정적 파일을 STATIC_ROOT 디렉터리로 복사)
"""
STATIC_ROOT = BASE_DIR / 'static/'
# BASE_DIR = /home/ubuntu/projects/mysite

"""
base.py 파일에 STATICFILES_DIRS 항목이 이미 있지만, prod.py 파일에 다시 빈 값으로 설정한다. 
그 이유는 STATIC_ROOT가 설정된 경우, 
STATICFILES_DIRS 리스트에 STATIC_ROOT와 동일한 디렉터리가 포함되어 있으면 서버 실행 시 오류가 발생한다.
"""
STATICFILES_DIRS = []
