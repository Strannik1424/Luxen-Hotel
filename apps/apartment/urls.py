from django.urls import path, include
from rest_framework import routers

from .views import *

# router = routers.SimpleRouter()
# router.register(r'apartment', ApartmentViewSets, basename='apartment')

urlpatterns = [
    path('', apartmentView, name='news'),
    path('about/', aboutApartment, name='about'),
    # path('api/v1/', include(router.urls)),
    
]


