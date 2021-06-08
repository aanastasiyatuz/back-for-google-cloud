from rest_framework import viewsets, generics,  status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PlaceSerializer, LodgingSerializer, CateringSerializer,\
                    PlaceImageSerializer, LodgingImageSerializer, CateringImageSerializer,\
                    CommentPlaceSerializer, CommentLodgingSerializer, CommentCateringSerializer
from .models import Place, Lodging, Catering,\
                    ImagePlace, ImageLodging, ImageCatering,\
                    CommentPlace, CommentLodging, CommentCatering


'''--------------------------PLACE---------------------------------'''
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    '''============Search by name============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(name__icontains=query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''============Search by address============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('address')
        queryset = self.get_queryset().filter(address__icontains=query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''===========Filter============='''
    @action(methods=['GET'], detail=False)
    def sort(self, request):
        filter = request.query_params.get('filter')
        if filter == 'A-Z':
            queryset = self.get_queryset().order_by('name')
        elif filter == 'Z-A':
            queryset = self.get_queryset().order_by('-name')
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaceImageView(generics.ListCreateAPIView):
    queryset = ImagePlace.objects.all()
    serializer_class = PlaceImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentPlace.objects.all()
    serializer_class = CommentPlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}



'''--------------------------LODGING---------------------------------'''
class LodgingViewSet(viewsets.ModelViewSet):
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer

    '''============Search by name============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(name__icontains=query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''============Search by address============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('address')
        queryset = self.get_queryset().filter(address__icontains=query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''===========Filter============='''
    @action(methods=['GET'], detail=False)
    def sort(self, request):
        filter = request.query_params.get('filter')
        if filter == 'A-Z':
            queryset = self.get_queryset().order_by('name')
        elif filter == 'Z-A':
            queryset = self.get_queryset().order_by('-name')
        elif filter == 'asc':
            queryset = self.get_queryset().order_by('average_check')
        elif filter == 'desc':
            queryset = self.get_queryset().order_by('-average_check')
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LodgingImageView(generics.ListCreateAPIView):
    queryset = ImageLodging.objects.all()
    serializer_class = LodgingImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentLodging.objects.all()
    serializer_class = CommentLodgingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}



'''--------------------------CATERING---------------------------------'''
class CateringViewSet(viewsets.ModelViewSet):
    queryset = Catering.objects.all()
    serializer_class = CateringSerializer

    '''============Search by name============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(name__icontains=query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''============Search by address============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('address')
        queryset = self.get_queryset().filter(address__icontains=query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''===========Filter============='''
    @action(methods=['GET'], detail=False)
    def sort(self, request):
        filter = request.query_params.get('filter')
        if filter == 'A-Z':
            queryset = self.get_queryset().order_by('name')
        elif filter == 'Z-A':
            queryset = self.get_queryset().order_by('-name')
        elif filter == 'asc':
            queryset = self.get_queryset().order_by('average_check')
        elif filter == 'desc':
            queryset = self.get_queryset().order_by('-average_check')
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CateringImageView(generics.ListCreateAPIView):
    queryset = ImageCatering.objects.all()
    serializer_class = CateringImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentCatering.objects.all()
    serializer_class = CommentCateringSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}
