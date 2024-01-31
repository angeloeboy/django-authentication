
from django.urls import path
from . import views
import dashboard


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("user/", views.get_dashboard),
    path("index/", views.index)

]