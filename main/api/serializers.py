from rest_framework import serializers
from .models import BusTime


class BusTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTime
        fields = ['id', 'time', 'where', 'destination', 'bus_number']