from django.urls import path
from . import views




urlpatterns = [
    path('teachers/', views.teachers, name = 'teachers'),
    path('students/', views.students, name = 'students'),
    path('login_message/', views.login_message, name = 'login_message'),
    path('student_details/<int:pk>', views.student_details, name = 'student_details'),
    
     
]