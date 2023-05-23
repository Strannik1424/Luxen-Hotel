from rest_framework import serializers 

from apps.contact.models import ContactModel, ContactModelForm

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'

class ContactFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactModelForm
        fields = '__all__'