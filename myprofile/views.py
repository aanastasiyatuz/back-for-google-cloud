from myprofile.models import ProfileProvider
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, mixins, status
from .serializers import ProfileClientSerializer, ProfileProviderSerializer
from .models import ProfileProvider, ProfileClient

MyUser = get_user_model()


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = ProfileProvider.objects.all()
    serializer_class = ProfileProviderSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = ProfileClient.objects.all()
    serializer_class = ProfileClientSerializer