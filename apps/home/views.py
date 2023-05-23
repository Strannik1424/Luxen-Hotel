from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


from .forms import *
from .models import BookNow

from apps.contact.models import ContactModel
from apps.apartment.forms import CommentForm
from apps.hoteInfo.models import Menu, TeamModel
from apps.apartment.models import ApartmentModel, Comment
from apps.home.api.serializers import BookNowSerializers



def home(req):
    newStellerForm = NewStellerForm()
    bookNowForm = OrderForm()
    menu = Menu.objects.all()

    if req.method == 'POST':
        bookNowForm = OrderForm(req.POST)
        newStellerForm = NewStellerForm(req.POST)
        if bookNowForm.is_valid():
            bookNowForm.save()
            newStellerForm.save()   

    newStellerForm = NewStellerForm()
    bookNowForm = OrderForm()
    contact = ContactModel.objects.order_by('-id')[0]
    homeRooms = ApartmentModel.objects.order_by('-id')[:3]

    context = {
        'bookNowForm':bookNowForm,
        'contact':contact,
        'homeRooms':homeRooms,
        'newStellerForm':newStellerForm,
        'menu':menu,
    }     
   
    return render(req, 'index.html', context)


def reservation(req):
    bookNowForm = OrderForm()

    if req.method == 'POST':
        bookNowForm = OrderForm(req.POST)
        if bookNowForm.is_valid():
            bookNowForm.save()
            bookNowForm = OrderForm()

    context = {
        'bookNowForm':bookNowForm,

    }
    return render(req, 'reservation.html', context)


def BlogDetailView(req, pk):
    comment = Comment.objects.filter(post=pk)
    posts_id = get_object_or_404(ApartmentModel, pk=pk)
    post = ApartmentModel.objects.filter(pk=pk)
    form = CommentForm()

    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            cmForm = form.save(commit=False)
            cmForm.post = posts_id
            cmForm.save()

    form = CommentForm()

    context = {
        'posts_id':posts_id,
        'posts':post,
        'commentForm':form,
        'comment':comment,
        'comment_count':comment.count()
    }
    return render(req, 'blog-detalis.html', context)


def PagesTeam(req):
    team = TeamModel.objects.order_by('-id')[:4]
    context = {
        'team':team
    }
    return render(req, 'team.html', context)


def CategoryGrid(req):
    apartment = ApartmentModel.objects.order_by('-id')[:6]
    context = {
        'apartment':apartment
    }
    return render(req, 'categoryGrid.html', context)


def Gallery(req):
    apartment = ApartmentModel.objects.all()
    context = {
        'apartment':apartment
    }
    return render(req, 'gallery.html', context)





class BookNowViewSet(viewsets.ModelViewSet):
    queryset = BookNow.objects.all()
    serializer_class = BookNowSerializers   






