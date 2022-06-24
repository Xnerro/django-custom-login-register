from django.views import View
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return JsonResponse({"msg": "failed to login"})
        print(user)
        login(request, user)
        return redirect("home")


class SignUpView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        print(form.errors)
        return JsonResponse({"msg": "register failed"})


class HomeView(View):
    def get(self, request):
        return JsonResponse({"msg": "welcome home"})
