from  . models import ride
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self,validated_data):
        user=get_user_model().objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=('username','password')


class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model=ride
        fields=['id','rider','driver','status_completed','date_Created','pickup_loc','dropoff_loc','status']


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model=ride
        fields = ['status']