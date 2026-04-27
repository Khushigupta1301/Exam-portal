
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import ExamFormSubmissionForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully. You are now logged in.')
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        next_url = request.POST.get('next')
        user = authenticate(
            request,
            username=request.POST.get('username', ''),
            password=request.POST.get('password', '')
        )
        if user:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('dashboard')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'next': request.GET.get('next', '')})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def fill_form(request):
    if request.method == "POST":
        form = ExamFormSubmissionForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return render(request, 'success.html', {'student_name': saved_form.full_name})
    else:
        form = ExamFormSubmissionForm()

    return render(request, 'form.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('signup')
