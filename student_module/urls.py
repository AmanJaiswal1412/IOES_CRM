from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.create_student, name='create_student'),
    path('student-profile/', views.student_profile, name='student_profile'),
    path('student-permanent-address/', views.student_permanent_address_view, name='student_permanent_address'),
    path('student-temp-address/', views.student_temp_address_view, name='student_temp_address'),
]
