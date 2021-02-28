from rest_framework import serializers

from api.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    """
    This serializer is responsible for handling serialization operations related to UserLogin
    """
    phone_number = serializers.CharField(max_length=10)
    password = serializers.CharField(
        max_length=100,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'password']
