from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views
from accounts.forms import LoginForm

urlpatterns = [
    path("piatti/", views.dishes, name="dishes"),
    path("piatti/<int:pk>/modifica/", views.dish_edit, name="dish_edit"),
    path("piatti/<int:pk>/elimina/", views.dish_delete, name="dish_delete"),
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registrazione/", views.register, name="register"),
]
