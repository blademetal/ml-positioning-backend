from rest_framework import serializers, viewsets
from .models import Beacons

class BeaconsSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Beacons
        fields = ('id', 'beacon_1', 'beacon_2', 'beacon_3', 'beacon_4', 'beacon_5', 'beacon_6', 'beacon_7', 'beacon_8')


class BeaconsViewSet(viewsets.ModelViewSet):
    queryset = Beacons.objects.all()
    serializer_class = BeaconsSerialiser