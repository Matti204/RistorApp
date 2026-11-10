from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views
from accounts.forms import LoginForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registrazione/", views.register, name="register"),
]
