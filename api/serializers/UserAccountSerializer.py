import re

import serializers as serializers
from rest_framework import serializers

from api.models import User


class UserAccountSerializer(serializers.ModelSerializer):
    """
    This serializer class will handle all the serialization functions for the User model.
    """
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=80)
    phone_number = serializers.CharField(max_length=10)
    # Keeping the password write_only as it is not meant to be returned
    password = serializers.CharField(min_length=8, max_length=12, write_only=True)
    account_created_on = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'account_created_on']

    def validate(self, attrs):
        phone_number = attrs.get('phone_number', '')
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Another user with the same phone number already exists')
        # Now we check if the password is having a valid strength
        """
        Password Strength Validation Parameters
        1. Minimum 8 characters.
        2. The alphabets must be between [a-z]
        3. At least one alphabet should be of Upper Case [A-Z]
        4. At least 1 number or digit between [0-9].
        5. At least 1 character from [ _@$!#%^&*() ]. 
        """
        if not self.validate_password_strength(attrs.get("password", '')):
            raise serializers.ValidationError('Your password do not possess a valid strength.')
        return super().validate(attrs)

    def create(self, validated_data):
        user = User(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    @staticmethod
    def validate_password_strength(password: str):
        if (len(password) < 8):
            return False
        elif not re.search("[a-z]", password):
            return False
        elif not re.search("[A-Z]", password):
            return False
        elif not re.search("[0-9]", password):
            return False
        elif not re.search("[_@$!#%^&*()]", password):
            return False
        elif re.search("\s", password):
            return False
        return True
