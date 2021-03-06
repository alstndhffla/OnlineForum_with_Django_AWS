from django.contrib import admin
from .models import Question
# 장고 Admin에서 모델 관리를 위해 위 모듈을 임포트

# Register your models here.


# 장고 공식 문서 주소(장고 Admin 기능): docs.djangoproject.com/en/3.0/ref/contrib/admin
# 장고 Admin에서 제목으로 질문을 검색할 수 있도록 검색 항목을 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


# 장고 셸로 수행했던 데이터 저장, 수정, 삭제 등의 작업을 장고 Admin에서 할 수 있다(모델관리)
# 아래 코드를 입력 후 장고 Admin으로 돌아가 새로고침 하면 Question 모델이 추가
admin.site.register(Question, QuestionAdmin)
