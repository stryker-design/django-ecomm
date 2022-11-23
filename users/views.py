from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from .forms import ManageAccountForm, NewUserForm


def registration(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, 'django.contrib.auth.backends.ModelBackend')
            return redirect('core:home')
        messages.error(request, "Unsuccessful registration. Invalid information.")

    context = {'form': form}

    return render(request, 'users/registration/registration.html', context)

def login_request(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user =authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home')
            else:
                messages.error(request,"Invalid username or password.")

    context = {'form': form}
    return render(request, 'users/registration/login.html', context)

def logout_request(request):
    logout(request)
    return redirect('core:home')


def account(request):
    context = {}
    return render(request, 'users/manage-account/account.html', context)


def manage_account(request):
    form = ManageAccountForm(request.POST, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('account') 
        else:
            return redirect('core:home')
    else:
        form = ManageAccountForm(instance=request.user)
        context = {'form': form}
        return render(request, 'users/manage-account/manage-account.html', context)

def test(request):
    pass