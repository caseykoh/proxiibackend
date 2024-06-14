from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from . models import *
from . serializer import *
from rest_framework.permissions import AllowAny

# @api_view(['GET', 'POST'])
# @permission_classes((AllowAny, ))

# Create your views here.

class InquirySubmissionView(viewsets.ModelViewSet):
    queryset = InquirySubmission.objects.all()
    serializer_class = InquirySubmissionSerializer

class AvailabilityView(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
