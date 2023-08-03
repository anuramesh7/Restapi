from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer,RideSerializer,UpdateSerializer
from.models import ride
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response

#
class RideViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ride.objects.all().order_by('-date_Created')
    serializer_class = RideSerializer

class CreateUserview(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class home(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RideSerializer

    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)

class RideStatusUpdateView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def update(self, request, pk=None):
        try:
            ride_instance = ride.objects.get(pk=pk)
        except ride.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateSerializer(ride_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return ride.objects.all().order_by('date_Created')
