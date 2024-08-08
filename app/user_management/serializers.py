from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)  # Explicitly set as required
    password = serializers.CharField(write_only=True, required=True)  # Required and write-only
    email = serializers.EmailField(required=True)  # Explicitly set as required

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user