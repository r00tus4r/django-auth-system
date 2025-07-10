from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome back, {0}!'.format(user.username))
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.', extra_tags='danger')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        messages.error(request, 'Please correct the errors bellow.', extra_tags='danger')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('dashboard')

def delete_account_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to delete your account.', extra_tags='danger')
        return redirect('login')

    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('register')

    return render(request, 'delete_account.html', {})

def profile_view(request, id):
    user = get_object_or_404(User, id=id)
    if request.user != user:
        messages.error(request, 'You do not have permission to view this profile.', extra_tags='danger')
        return redirect('dashboard')
    return render(request, 'profile.html', {'user': user})

def update_profile_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to update your profile.', extra_tags='danger')
        return redirect('login')

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', id=request.user.id)
        messages.error(request, 'Please correct the errors below.', extra_tags='danger')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

def dashboard_view(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change-password')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})
