from django.urls import path, include

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('team/', PagesTeam, name='team'),
    path('gallery/', Gallery, name='gallery'),
    path('', include('apps.home.api.routers')),
    path('reservation/', reservation, name='reservation'),
    path('categoryGrid/', CategoryGrid, name='categoryGrid'),
    path('post/<int:pk>/', BlogDetailView, name='post_detail'),
]


