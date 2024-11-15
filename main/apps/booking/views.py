from main.apps.booking.models import Booking
from ..booking.serializers import BookingSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

booking_create_api_view = BookingCreateAPIView.as_view()


class BookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
booking_list_api_view = BookingListAPIView().as_view()


class BookingDeleteAPIView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object() 
        self.perform_destroy(instance)
        return Response({"message": "Booking deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

booking_delete_api_view = BookingDeleteAPIView().as_view()