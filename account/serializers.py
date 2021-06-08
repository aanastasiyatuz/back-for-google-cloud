from django.contrib.auth import get_user_model
from rest_framework import serializers
from myprofile.models import ProfileProvider, ProfileClient

MyUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password_confirmation = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ('email', 'phone', 'password', 'password_confirmation', 'status')

    def validate_email(self, email):
        if MyUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с данным email уже существует')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation', None)
        if password != password_confirmation:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        if user.status == 'provider':
            ProfileProvider.objects.create(user=user, email=user.email)
        else:
            ProfileClient.objects.create(user=user, email=user.email)
        return user
