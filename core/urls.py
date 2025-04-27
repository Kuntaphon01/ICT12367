from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='home'),  # เพิ่มที่นี่
    path('form/', views.activity_form, name='activity_form'),
    path('list/', views.activity_list, name='activity_list'),
    path('edit/<int:pk>/', views.activity_edit, name='activity_edit'),
    path('delete/<int:pk>/', views.activity_delete, name='activity_delete'),
]