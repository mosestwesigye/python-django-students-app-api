from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = "home"),
    path('student-view/<str:pk>/', views.studentView, name="studentview"),
    path('add-student', views.studentAdd, name="add-student"),
    path('update-student/<str:pk>/', views.studentUpdate, name="studentupdate"),
    path('delete-student/<str:pk>/', views.studentDelete, name="studentdelete")
]
