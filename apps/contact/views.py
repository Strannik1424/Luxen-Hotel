from django.shortcuts import render
from rest_framework import viewsets

from apps.contact.models import ContactModel, ContactModelForm
from apps.contact.api.serializers import ContactSerializers, ContactFormSerializers
from apps.contact.forms import ContactForm
from apps.hoteInfo.models import HotelInfo


def ContactView(req):
    if req.method == 'POST':
        contactForm = ContactForm(req.POST)
        contactForm.save()
    contactForm = ContactForm()

    modelContact = ContactModel.objects.order_by('-id')[0]
    hotelInfo = HotelInfo.objects.order_by('-id')[0]
    

    context = {
        'contact':modelContact,
        'contactForm':contactForm,
        'hotelInfo':hotelInfo
    }
    return render(req, 'contact.html', context)


def blogContact(req):
    modelContact = ContactModel.objects.all()

    context = {
        'modelContact':modelContact,
    }
    return render(req, 'blog.html', context)


def FooterContact(req):
    modelContact = ContactModel.objects.order_by('-id')[0]

    context = {
        'contact':modelContact,
    }
    return render(req, 'index.html', context)




class ContactViewSets(viewsets.ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializers


class ContactFormViewSets(viewsets.ModelViewSet):
    queryset = ContactModelForm.objects.all()
    serializer_class = ContactFormSerializers