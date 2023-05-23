from rest_framework import serializers

from apps.apartment.models import ApartmentModel

class ApartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model  = ApartmentModel 
        fields = '__all__'