from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages/', views.task_list, name='task_list'),
    path('pages/<int:pk>/', views.task_detail, name='task_detail'),
    path('pages/<int:pk>/done/', views.task_done, name='task_done'),
]
