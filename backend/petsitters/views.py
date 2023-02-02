# from django.shortcuts import render

# Create your views here.


from .models import Petsitter
from pets.models import Pet
from pets.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

@api_view(['GET','POST'])
def petsitters_list(request):
    # permission_classes = (permissions.AllowAny, )
    if request.method == 'GET':
        data = Petsitter.objects.all()
        serializer = PetsitterSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        
        serializer = PetsitterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            # print(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#did not work
# @authentication_classes([])
# @permission_classes([])  
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def petsitters_detail(request, pk):
    # permission_classes = (permissions.AllowAny, )
    try:
        petsitter = Petsitter.objects.get(pk=pk)
    except Petsitter.DoesNotExist:
        return Response({"msg": f"Can not find petsitter with id {pk}"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PetsitterSerializer(petsitter, context={'request': request})
        # pets = petsitter.pets.all()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        serializer = PetsitterSerializer(petsitter, data=request.data,context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = PetsitterSerializer(petsitter, data=request.data,context={'request': request})
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Petsitter successfully updated', status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        petsitter.delete()
        return Response('Petsitter successfully deleted', status=status.HTTP_200_OK)

@api_view(['GET'])
def petsitters_detail_pets_list(request, pk):
    # permission_classes = (permissions.AllowAny, )
    try:
        petsitter = Petsitter.objects.get(pk=pk)
    except Petsitter.DoesNotExist:
        return Response({"msg": f"Can not find petsitter with id {pk}"},status=status.HTTP_404_NOT_FOUND)
    
    pets = petsitter.pets.all()
   
    if request.method == 'GET':
      
        pets_list = []
        for pet in pets:
            pet_dict = {
                "pk": pet.pk,
                "pet_name": pet.pet_name,
                "pet_type_needs_care": pet.pet_type_needs_care,
                "pet_needs_description": pet.pet_needs_description,
                "is_needs_care": pet.is_needs_care,
                "petsitter": pet.petsitter.name
                # "pet_photo": pet.pet_photo
            }
            pets_list.append(pet_dict)
       
        return Response(pets_list, status=status.HTTP_200_OK) #working
       
    # elif request.method == 'PUT':
    #     serializer = PetsitterSerializer(petsitters_list, data=request.data,context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response('Petsitter successfully updated', status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
    #     petsitter.delete()
    #     return Response('Petsitter successfully deleted', status=status.HTTP_200_OK)
