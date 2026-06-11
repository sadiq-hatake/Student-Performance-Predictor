from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('students/', views.students, name='students'),
    path('details/<int:id>/', views.details, name='details'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]