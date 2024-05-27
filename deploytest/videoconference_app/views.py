from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'videoconference_app/login.html', {'success': "Registration successful. Please log in."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'videoconference_app/register.html', {'form': form, 'error_message': error_message})
    
    return render(request, 'videoconference_app/register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'videoconference_app/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'videoconference_app/dashboard.html')
@login_required
def videocall(request):
    return render(request, 'videoconference_app/videoapp.html',{'name':request.user.username})
