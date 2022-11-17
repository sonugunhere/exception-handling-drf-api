from django.urls import path
from .import views


urlpatterns=[
    
    path('list', views.StudentList.as_view(), name = 'list'),
    path('student/<int:pk>/', views.StudentApi.as_view(), name = 'student'),
    path('', views.EventApi.as_view(), name = 'event'),
    
    
]