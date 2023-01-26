from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Petsitter
from .serializers import *

# from rest_framework import permissions
# from rest_framework.decorators import authentication_classes, permission_classes
#to disable authenfication

#try add this check if user is authenticated later
# from rest_framework.permissions import IsAuthenticated
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])

#did not work
# @authentication_classes([])
# @permission_classes([])
@api_view(['GET','POST'])
def petsitters_list(request):
    # permission_classes = (permissions.AllowAny, )
    if request.method == 'GET':
        data = Petsitter.objects.all()
        serializer = PetsitterSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PetsitterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#did not work
# @authentication_classes([])
# @permission_classes([])  
@api_view(['GET', 'PUT', 'DELETE'])
def petsitters_details(request, pk):
    # permission_classes = (permissions.AllowAny, )
    try:
        petsitter = Petsitter.objects.get(pk=pk)
    except Petsitter.DoesNotExist:
        return Response({"msg": f"Can not find petsitter with id {pk}"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PetsitterSerializer(petsitter)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PetsitterSerializer(petsitters_list, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response('Petsitter successfully updated', status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        petsitter.delete()
        return Response('Petsitter successfully deleted', status=status.HTTP_200_OK)
