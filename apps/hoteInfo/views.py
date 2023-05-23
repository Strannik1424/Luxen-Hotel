from django.shortcuts import render
from rest_framework import viewsets

from apps.hoteInfo.models import HotelInfo, Sidebar, TeamModel
from apps.hoteInfo.api.serializers import HotelInfoSerializers, SidebarSerializers, TeamSerializers
from apps.contact.models import ContactModel
# Create your views here.


class HotelInfoViewSets(viewsets.ModelViewSet):
    queryset = HotelInfo.objects.all()
    serializer_class = HotelInfoSerializers


class SidebarViewSets(viewsets.ModelViewSet):
    queryset = Sidebar.objects.all()
    serializer_class = SidebarSerializers


class TeamViewSets(viewsets.ModelViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = TeamSerializers


def AboutSidebar(req):
    sidebar = Sidebar.objects.order_by('-id')[0]
    context = {
        'sidebar':sidebar,
    }
    return render(req, 'about.html', context)


def FooterContact(req):
    modelContact = ContactModel.objects.order_by('-id')[0]

    context = {
        'contact':modelContact,
    }
    return render(req, 'about.html', context)


