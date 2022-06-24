from django.urls import path
from .views import HomeView, LoginView, SignUpView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", login_required(HomeView.as_view(), login_url="login"), name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
]
