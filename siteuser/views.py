from django.http import Http404
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from .models import CustomUserModel
from django.core.exceptions import ObjectDoesNotExist


def registration_view(request):
    page_title = 'registration'
    if request.user.id is not None:
        return render(request, template_name='universal_error.html', context={
            'error': 'You are already registered'
        })
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                del form.cleaned_data['confirm_password']
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                form.save()
                # obj = CustomUser.objects.get(username=form.cleaned_data['username'])
                return redirect('login')
        else:
            form = RegistrationForm()

        return render(request, template_name='user_registration.html', context={
            'form': form,
            'page_title': page_title
        })


def login_view(request):
    page_title = 'login'
    if request.user.is_authenticated:
        return render(request, 'universal_error.html', context={
            'error': 'You are already logged in'
        })
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('home')
                form.add_error('password', 'Username or Password was incorrect!')

        return render(request, template_name='login.html', context={
            'form': form,
            'page_title': page_title
        })


def logout_view(request):
    logout(request)
    return redirect('home')
