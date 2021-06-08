from rest_framework import serializers
from .models import Place, Lodging, Catering,\
                    ImagePlace, ImageLodging, ImageCatering,\
                    CommentPlace, CommentLodging, CommentCatering



'''--------------------------PLACE---------------------------------'''
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = PlaceImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['comments'] = CommentPlaceSerializer(instance.comments.all(), many=True, context=self.context).data
        return representation


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePlace
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation

class CommentPlaceSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)

    class Meta:
        model = CommentPlace
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create' or action == 'update':
            fields.pop('author')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = CommentPlace.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance




'''--------------------------LODGING---------------------------------'''
class LodgingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lodging
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = LodgingImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['comments'] = CommentLodgingSerializer(instance.comments.all(), many=True, context=self.context).data
        return representation


class LodgingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLodging
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation

class CommentLodgingSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)

    class Meta:
        model = CommentLodging
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create' or action == 'update':
            fields.pop('author')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = CommentLodging.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance




'''--------------------------CATERING---------------------------------'''
class CateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = CateringImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['comments'] = CommentCateringSerializer(instance.comments.all(), many=True, context=self.context).data
        return representation


class CateringImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCatering
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation

class CommentCateringSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)

    class Meta:
        model = CommentCatering
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create' or action == 'update':
            fields.pop('author')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = CommentCatering.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance