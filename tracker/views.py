from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import log_request, reset_table

# Create your views here.


def index(request):
    
    numbers = list(range(37))  # Generates numbers from 0 to 36
     
    return render(request, 'index.html', {'numbers': numbers})



class NumberPressView(APIView):
    def patch(self, request, number, *args, **kwargs):

        # Ensure the number is provided and is within the valid range (0–36)
        if number is None or not (0 <= int(number) <= 36):
            return Response({"error": "Invalid number"}, status=status.HTTP_400_BAD_REQUEST)

        # Create entry in DB
        response = log_request(number)

        # Respond with a success message
        return Response(response, status=status.HTTP_200_OK)


class ResetTableView(APIView):
    def delete(self, request, table, *args, **kwargs):
        
        response = reset_table(table)
        
        # Respond with a success message
        return Response(response, status=status.HTTP_200_OK)