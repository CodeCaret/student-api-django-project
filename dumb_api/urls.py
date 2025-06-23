from django.urls import path
from dumb_api import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('student/<int:pk>/', views.get_update_delete_student, name='individual-student')
]