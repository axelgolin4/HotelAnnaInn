from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


