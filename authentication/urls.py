
from django.urls import path

from dashboard.views import dashboard
from . import views

urlpatterns = [
    path("login/", views.login ),
    path('register/', views.register, name='register'),
    path('test/', views.test_token, name='test'),
    path('dashboard/', dashboard, name='dashboard')
]
