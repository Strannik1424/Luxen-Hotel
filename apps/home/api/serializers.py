from rest_framework import serializers

from apps.home.models import BookNow


class BookNowSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookNow
        fields = "__all__"

