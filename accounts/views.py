from django.shortcuts import render , redirect
from django.contrib.auth.models import User

def login(request):
    return render(request, "accounts/login.html")

def register(request):
  
    if request.method == "POST":
        input_username = request.POST.get("username")
        input_password = request.POST.get("password")

        new_user = User(
            username = input_username
        )

        new_user.set_password(input_password)

        new_user.save()

        return redirect("login")

    return render(request, "accounts/register.html")


