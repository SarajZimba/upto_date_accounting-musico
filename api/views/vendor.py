from purchase.models import Vendor
from rest_framework.views import APIView
from api.serializers.vendor import VendorSerializer
from rest_framework.response import Response

class VendorCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = VendorSerializer(data=data)
        try:
            if serializer.is_valid():
                serializer.save()   
                return Response("Vendor Created Successfully", 200)
        except Exception as e:
            return Response({"detail":f"Error creatind vendor" + str(e)}, 400)

        
