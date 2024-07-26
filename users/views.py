from django.shortcuts import render


def login_user(request):
    context = {"page_title": "Login"}
    return render(request, "users/login.html", context=context)


def register_user(request):
    context = {"page_title": "Register User"}
    return render(request, "users/register_user.html", context=context)
