from field.serializers import FieldSerializer
from ..field.models import Field
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status




class FieldCreateAPIView(generics.CreateAPIView):
    serializer_class = FieldSerializer()
    queryset = Field.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            cashbox = serializer.save()
            return Response(status_code=status.HTTP_201_CREATED, data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(status_code=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    

field_create_api_view = FieldCreateAPIView().as_view()



class AvailableField(generics.ListAPIView):
    serializer_class = FieldSerializer()

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        location = self.request.query_params.get('location')

        qs = Field.objects.all()

        if start_time and end_time:
            qs = qs.exclude(
                booking__start_time__lt=end_time,
                booking__end_time__gt=start_time,
                booking_is_active=True
            )
        return qs 