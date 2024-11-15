from main.apps.user.models import UserProfile
from main.apps.user.serializers import UserProfileSerializer
from ..field.serializers import FieldSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status



class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

user_create_api_view = UserCreateAPIView.as_view()