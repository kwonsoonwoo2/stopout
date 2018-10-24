from django.urls import path

from . import views

app_name = 'school'
urlpatterns = [
    path('', views.index, name='index'),
    path('school/', views.school_list, name='school-list'),
    path('school/<int:school_id>/', views.school_detail, name='school-detail'),
    path('student/', views.student_list, name='student-list'),
    path('student/<int:student_id>/', views.student_detail, name='student-detail'),
]