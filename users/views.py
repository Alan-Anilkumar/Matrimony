from django.shortcuts import render

from users.forms import CustomUserCreationForm


def login_user(request):
    context = {"page_title": "Login"}
    return render(request, "users/login.html", context=context)


def register_user(request):
    if request.method == "POST":
        pass
    else:
        form = CustomUserCreationForm()
    context = {"page_title": "Register User", "form": form}
    return render(request, "users/register_user.html", context=context)
