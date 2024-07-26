from django.urls import path

import users.views as views

urlpatterns = [
    path("", views.login_user, name="login_user"),
    path("user/register/", views.register_user, name="register_user"),
]
