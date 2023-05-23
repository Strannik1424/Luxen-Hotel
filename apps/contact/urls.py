from django.urls import path, include

from apps.contact.views import ContactView

urlpatterns = [
    path('', ContactView, name='contact')
]
