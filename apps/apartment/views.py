from django.shortcuts import render
from rest_framework import viewsets

from .models import ApartmentModel, Comment
from apps.apartment.forms import CommentForm
from apps.apartment.api.serializers import ApartmentSerializers
from apps.contact.models import ContactModel
from apps.hoteInfo.models import HotelInfo

def apartmentView(req):
    comment = Comment.objects.all()
    all_model = ApartmentModel.objects.order_by('-id')[:3]
    contact = ContactModel.objects.order_by('-id')[0]
    info = HotelInfo.objects.order_by('-id')[0]
    recentNews = ApartmentModel.objects.order_by('id')[:2]

    comments_counts = {}

    for post in all_model:
        comments = Comment.objects.filter(post=post)
        comments_counts[post.id] = comments.count()

    context = {
        'all_model':all_model,
        'contact':contact,
        'info':info,
        'recentNews':recentNews,
        'comments_counts':comments_counts
    }
    return render(req, 'blog.html', context)



def aboutApartment(req):
    aboutHotels = ApartmentModel.objects.order_by('-id')[0]
    slideAbout = ApartmentModel.objects.order_by('-id')[1:4]

    context = {
        'aboutHotels':aboutHotels,
        'slideAbout':slideAbout
    }

    return render(req, 'about.html', context)


def blogDetalis(req):
    commentForm = CommentForm()
    contact = ContactModel.objects.order_by('-id')[0]
    recentNews = ApartmentModel.objects.order_by('id')[:2]

    print('*'*30)
    print(contact)
    context = {
        'commentForm':commentForm,
        'contact':contact,
        'recentNews':recentNews
    }
    return render(req, 'blog-detalis.html', context)


class ApartmentViewSets(viewsets.ModelViewSet):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentSerializers


