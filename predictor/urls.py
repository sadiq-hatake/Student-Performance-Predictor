from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('details/<int:id>/', views.details, name='details'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('dashboard/', views.dashboard, name='dashboard'),
]