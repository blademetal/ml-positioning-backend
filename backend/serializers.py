from rest_framework import serializers

from .models import Beacons

class BeaconsSerializer(serializers.Serializer):
    beacon_1 = serializers.IntegerField()
    beacon_2 = serializers.IntegerField()
    beacon_3 = serializers.IntegerField()
    beacon_4 = serializers.IntegerField()
    beacon_5 = serializers.IntegerField()
    beacon_6 = serializers.IntegerField()
    beacon_7 = serializers.IntegerField()
    beacon_8 = serializers.IntegerField()

    def create(self, validated_data):
        return Beacons.objects.create(**validated_data)