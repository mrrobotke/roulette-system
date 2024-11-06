from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import log_request

# Create your views here.

class IndexView(APIView):

    def index(self, request):
        numbers = list(range(37))  # Creates a list of numbers from 0 to 36
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
