from django.apps import AppConfig


# 이 파일은 forum 앱을 만들 때 자동으로 생성된 것
# 이 파일에 정의된 forumConfig 클래스가 config/settings.py 파일의 INSTALLED_APPS 항목에
# 추가되지 않으면 장고는 forum 앱을 인식하지 못하고 데이터베이스 관련 작업도 할 수 없다
class forumConfig(AppConfig):
    name = 'forum'
