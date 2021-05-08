from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from . import models
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
