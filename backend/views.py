from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Beacons
from .serializers import BeaconsSerializer


class BeaconsView(APIView):
    def get(self, request):
        articles = Beacons.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = BeaconsSerializer(articles, many=True)
        return Response({"beacons": serializer.data})
    
    def post(self, request):
        beacons = request.data.get('beacons')

        # Create an beacons from the above data
        serializer = BeaconsSerializer(data=beacons)
        if serializer.is_valid(raise_exception=True):
            beacon_saved = serializer.save()
        return Response({"success": "Beacon '{}' created successfully"})
