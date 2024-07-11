from django.urls import path
from . import views

from .views import SignUpView
from django.views.generic.base import TemplateView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('/submit_action', views.google_analyz, name='submit_action'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),


]
