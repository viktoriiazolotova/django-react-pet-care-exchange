# # Create your views here.
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView

# from .models import Pet
# from .serializers import PetSerializer, petDetailSerializer
# from rest_framework import permissions

# class PetsView(ListAPIView):
#     queryset=Pet.objects.all()
#     serializer_class = PetSerializer
#     lookup_field='pk'

# class PetView(ListAPIView):
#     queryset = Pet.objects.order_by('pk')
#     serializer_class = petDetailSerializer
#     lookup_field = 'pk'

# class SearchView(APIView):
   
#     serializer_class = PetSerializer
   
#     def post(self, request, format=None):
#         queryset = Pet.objects.order_by('pk')
#         data = self.request.data

#         pet_type = data['pet_type']
#         queryset = queryset.filter(pet_type__iexact=pet_type)
#         serializer = PetSerializer(queryset, many=True)

#         return Response(serializer.data)


#functional view
from .models import Pet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

@api_view(['GET','POST'])
def pets_list(request):

    if request.method == 'GET':
        data = Pet.objects.all()
        serializer = PetSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pet_detail(request, pk):
    # permission_classes = (permissions.AllowAny, )
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response({"msg": f"Can not find pet with id {pk}"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PetSerializer(pet)
        # pets = petsitter.pets.all()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PetSerializer(pets_list, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response('Pet successfully updated', status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pet.delete()
        return Response('Pet successfully deleted', status=status.HTTP_200_OK)