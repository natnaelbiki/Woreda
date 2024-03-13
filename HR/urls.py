from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff/list', views.staff_list, name='staff_list'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/edit/<int:pk>/', views.edit_staff, name='edit_staff'),
    path('staff/delete/<int:pk>/', views.delete_staff, name='delete_staff'),
]
