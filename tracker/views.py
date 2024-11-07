from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .configs import logger
from rest_framework import status
from .models import NumberStatistics
from .utils import generate_password, log_request, reset_table
from django.contrib.auth.hashers import make_password
import json

# Create your views here.


@csrf_exempt
def generate_and_send_password(request):
    logger.info(f"Request: {request.body}")
    if request.method == 'POST':
        email = json.loads(request.body)['email']

        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        # Generate a password
        password = generate_password()
        hashed_password = make_password(password)
        
        user = User.objects.get(email=email)
        user.password = hashed_password  # Update the user's password
        user.save()

        # Send the email with the password
        subject = 'Roulette Generated Password'
        message = f'Your password generated is: {password}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

        return JsonResponse({"message": "Password generated and sent to your email."}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)



def index(request):
    
    numbers = list(range(37))  # Generates numbers from 0 to 36
     
    return render(request, 'index.html', {'numbers': numbers})


def log_number_endpoint(request):
        
        if request.method == 'POST':
            
            data = json.loads(request.body.decode('utf-8'))
            
            logger.info(f"Json Payload: {data}")
            
            number = data['number']
            color = data['color']
            parity = data['parity']
            range_value = data['range']
            

            # Ensure the number is provided and is within the valid range (0–36)
            if number is None or not (0 <= int(number) <= 36):
                return Response({"error": "Invalid number"}, status=status.HTTP_400_BAD_REQUEST)
            
            if color is None or color not in ['r', 'b', 'g']:
                return Response({"error": "Invalid color"}, status=status.HTTP_400_BAD_REQUEST)
            
            if parity is None or parity not in ['e', 'o']:
                return Response({"error": "Number can only be odd or even"}, status=status.HTTP_400_BAD_REQUEST)
            
            if range_value is None or range_value not in ['h', 'l']:
                return Response({"error": "Invalid range"}, status=status.HTTP_400_BAD_REQUEST)
            

            # Create entry in DB
            try:
                NumberStatistics.objects.create(number=number, 
                                                color=color, 
                                                parity=parity, 
                                                range_value=range_value)
                
                # Respond with a success message
                return JsonResponse({'message':'Record saved successfully'}, status=status.HTTP_200_OK)
                
            except Exception as e: 

                # Respond with an error message
                response = {'message': f'Error {type(e).__name__} - {str(e)}'}
                return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        else:
            
            response = {'message': f'{request.method} method not allowed'}
            return JsonResponse(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ResetTableView(APIView):
    def delete(self, request, table, *args, **kwargs):
        
        response = reset_table(table)
        
        # Respond with a success message
        return Response(response, status=status.HTTP_200_OK)