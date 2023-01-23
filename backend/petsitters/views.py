from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Petsitter
from .serializers import *

from rest_framework import permissions

@api_view(['GET','POST'])
def petsitters_list(request):
    permission_classes = (permissions.AllowAny, )
    if request.method == 'GET':
        data = Petsitter.objects.all()
        serializer = PetsitterSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PetsitterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE'])
def petsitters_details(request, pk):
    try:
        petsitter = Petsitter.objects.get(pk=pk)
    except Petsitter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = PetsitterSerializer(petsitters_list, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        petsitter.delete()
        return Response(status=status.HTTP_200_OK)
