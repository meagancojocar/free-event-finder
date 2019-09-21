from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Register.as_view(), name='login'),
    path('logout/', views.Register.as_view(), name='logout'),
]