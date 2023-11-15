from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Registration
from .serializers import RegistrationSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CancelRegistrationView(APIView):
    def post(self, request):
        national_id = request.data.get('national_id')
        registration = get_object_or_404(Registration, national_id=national_id)
        registration.canceled = True
        registration.save()
        return Response({'message': 'Cancellation successful'})


class ListRegistrationsView(APIView):
    def get(self, request):
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)

def register_form(request):
    return render(request, 'registration/register_form.html')

def registration_list(request):
    filter_criteria = request.GET.get('filter', 'all')
    if filter_criteria == 'canceled':
        registrations = Registration.objects.filter(canceled=True)
    elif filter_criteria == 'not_canceled':
        registrations = Registration.objects.filter(canceled=False)
    else:
        registrations = Registration.objects.all()
    return render(request, 'registration/registration_list.html', {'registrations': registrations, 'filter_criteria': filter_criteria})

def cancel_form(request):
    return render(request, 'registration/cancel_form.html')

