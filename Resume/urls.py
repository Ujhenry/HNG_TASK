
from django.urls import path
from . import views

app_name = "Resume"

urlpatterns = [
    path("", views.home, name="home"),
]