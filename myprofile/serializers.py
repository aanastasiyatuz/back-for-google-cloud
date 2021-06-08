from rest_framework import serializers
from .models import ProfileClient, ProfileProvider


class ProfileClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileClient
        fields = '__all__'


class ProfileProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileProvider
        fields = '__all__'