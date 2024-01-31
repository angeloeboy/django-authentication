
from django.urls import include, path

# from dashboard import dashboard
from . import views

urlpatterns = [
    path("login/", views.login ),
    path('register/', views.register, name='register'),
    path('test/', views.test_token, name='test'),
    # path('dashboard/', include(dashboard.urls))
    path('dashboard/', include('dashboard.urls'))
]
