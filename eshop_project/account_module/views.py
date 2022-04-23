from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.base import View

from account_module.forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context ={
            'register_form': register_form
        } 
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            # todo: register user
            pass

        context ={
            'register_form': register_form
        } 
        return render(request, 'account_module/register.html', context)