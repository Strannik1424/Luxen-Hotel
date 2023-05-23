from rest_framework import serializers

from apps.hoteInfo.models import HotelInfo, Sidebar, TeamModel


class HotelInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelInfo
        fields = '__all__'

class SidebarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sidebar
        fields = '__all__'

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'
