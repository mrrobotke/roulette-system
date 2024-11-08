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
from rest_framework import status
import json
from tracker.configs import logger
from tracker.utils import get_machine_id

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            login_form = LoginForm()
        
            return render(request, 'registration/register.html', {'form': login_form})
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
            
            # Authenticate the user here
            user = authenticate(request, username=username, password=password)
            if user is None:
                # Authentication failed
                logger.info('Invalid credentials')
                messages.error(request, 'Invalid username or password.')
                

            # Retrieve user details if authenticated
            user_details = list(User.objects.filter(username=username).values())
            
            # Check if user is registered
            if len(user_details) == 0:
                logger.info('User is not registered')
                messages.error(request, 'User does not exist. Register to create your account.')
                # return JsonResponse({'error': 'User does not exist. Register to create your account.'}, safe=False, status=400)
            
            user_id = user_details[0]['id']
            
            # Check client UUID for the authenticated user
            frontend_user = list(UserProfile.objects.filter(user_id=user_id).values())
            if frontend_user:
                client_uuid = frontend_user[0]['client_uuid']
                
                if client_uuid != get_machine_id():
                    logger.info("Unauthorized access")
                    messages.error(request, 'Unauthorized access')
                    # return JsonResponse({'error': 'You do not have access to this resource.'}, safe=False, status=401)

            
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
            UserProfile.objects.create(user=user, phone_number=phone_number, client_uuid=get_machine_id())

            return JsonResponse({"message": "Registration successful"}, status=201)

        except IntegrityError:
            logger.error(f"Error: username/email already exists")
            return JsonResponse({"error": "Username or email already exists"}, status=400)
        except Exception as e:
            logger.error(f"Error: {type(e).__name__} - {str(e)}")
            
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

# Login view
def login_endpoint(request):
    
    if request.method == 'POST':
    
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # Authenticate the user here
            user = authenticate(request, username=username, password=password)
            if user is None:
                # Authentication failed
                logger.info('Invalid credentials')
                JsonResponse({'error': 'Invalid username or password.'}, status=400)
                

            # Retrieve user details if authenticated
            user_details = list(User.objects.filter(username=username).values())
            
            # Check if user is registered
            if len(user_details) == 0:
                logger.info('User is not registered')
                messages.error(request, 'User does not exist. Register to create your account.')
                return JsonResponse({'error': 'Invalid username or password'}, status=400)
            
            user_id = user_details[0]['id']
            
            # Check client UUID for the authenticated user
            frontend_user = list(UserProfile.objects.filter(user_id=user_id).values())
            if frontend_user:
                client_uuid = frontend_user[0]['client_uuid']
                
                if client_uuid != get_machine_id():
                    logger.info("Unauthorized access")
                    messages.error(request, 'Unauthorized access')
                    return JsonResponse({'error': 'You do not have access to this resource.'}, status=401)

            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return JsonResponse({'success': 'Login successful.'}, status=200)

            else:
                messages.error(request, 'Invalid credentials')
                return JsonResponse({'error': 'Invalid username or password'}, status=400)
            
        except Exception as e:
            logger.error(f"Error: {type(e).__name__} - {str(e)}")
            
            return JsonResponse({"error": str(e)}, status=500)    
                
    return JsonResponse({"error": "Invalid request method"}, status=405)
