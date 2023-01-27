from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Pet
from .serializers import PetSerializer, petDetailSerializer
from rest_framework import permissions

class PetsView(ListAPIView):
    # permission_classes = (permissions.AllowAny, )
    queryset=Pet.objects.all()
    serializer_class = PetSerializer
    lookup_field='pk'

class PetView(ListAPIView):
    # permission_classes = (permissions.AllowAny, )
    queryset = Pet.objects.order_by('pk')
    serializer_class = petDetailSerializer
    lookup_field = 'pk'

class SearchView(APIView):
   
    serializer_class = PetSerializer
    # permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        queryset = Pet.objects.order_by('pk')
        data = self.request.data

        pet_type = data['pet_type']
        queryset = queryset.filter(pet_type__iexact=pet_type)
        serializer = PetSerializer(queryset, many=True)

        return Response(serializer.data)