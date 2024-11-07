from django.shortcuts import render

# Create your views here.

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import User
from django.db import IntegrityError
import json
from tracker.configs import logger

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to home or another page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')  # Redirect to home or another page
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@csrf_exempt
def register_endpoint(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            username = data.get('username')
            phone_number = data.get('phone_number')
            
            logger.info(f"Data: {data}")

            if not email or not username or not phone_number:
                return JsonResponse({"error": "All fields are required"}, status=400)

            # Create the User object
            user = User.objects.create_user(username=username, email=email)
            user.save()

            # Create the UserProfile with the phone number
            UserProfile.objects.create(user=user, phone_number=phone_number)

            return JsonResponse({"message": "Registration successful"}, status=201)

        except IntegrityError:
            logger.error(f"Error: username/email already exists")
            return JsonResponse({"error": "Username or email already exists"}, status=400)
        except Exception as e:
            logger.error(f"Error: {type(e).__name__} - {str(e)}")
            
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)