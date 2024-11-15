from ..field.serializers import FieldSerializer
from ..field.models import Field
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status




class FieldCreateAPIView(generics.CreateAPIView):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
        response_data = {
            "message": "Field created successfully!",
            "field": serializer.data
        }
        return Response(status=status.HTTP_201_CREATED, data=response_data)

    

field_create_api_view = FieldCreateAPIView().as_view()



class FieldListAPIView(generics.ListAPIView):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()

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
    
field_list_api_view = FieldListAPIView().as_view()

class FieldDetailAPIView(generics.RetrieveAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    # permission_classes = [permissions.IsAuthenticated]

field_detail_api_view = FieldDetailAPIView.as_view()


class FieldUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [permissions.IsAuthenticated]


field_update_api_view = FieldUpdateAPIView().as_view()