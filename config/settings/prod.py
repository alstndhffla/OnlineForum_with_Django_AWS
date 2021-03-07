from .base import *
"""
서버 환경 담당파일
"""


# AWS 서버 고정 ip 등록, 가비아에서 구입한 도메인 'quantforum.kr' 추가
ALLOWED_HOSTS = ['3.34.54.66', 'quantforum.kr']

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

"""
장고는 실행 도중에 오류가 발생하면 DEBUG가 True인 경우, 오류 내용을 브라우저에 상세하게 출력.
그러면 settings.py 파일 등애 설정 항목들이 노출된다(서버정보가 보인다)
"""
DEBUG = False

# 서버에 설치한 postgreSQL 에 접속하기 위해.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'forum',
        'USER': 'dbmasteruser',
        'PASSWORD': 'za5870za',
        'HOST': 'ls-0f369f631f262ea24a2be84d4a0aca67d43ade26.czz5gkwznb9w.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}