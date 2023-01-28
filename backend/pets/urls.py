from django.urls import path
from .views import PetsView, PetView, SearchView

#/pets/
urlpatterns = [
    path('', PetsView.as_view()),
    path('<int:pk>',PetView.as_view()),
    path('search', SearchView.as_view())

]