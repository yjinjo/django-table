from django.urls import path

from . import views

urlpatterns = [
    # 레스트랑의 리스트를 보여주는 화면을 연결합니다.
    path('list/', views.list, name="list"),
]
