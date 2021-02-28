from rest_framework import serializers

from api.models import ProfessionalInfo, User


class ProfessionalInfoSerializer(serializers.ModelSerializer):
    """
    This serializer shall be responsible for handling all serializing operations related to ProfessionalInfo
    """
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    phone_number = serializers.CharField(source="user.phone_number", read_only=True)
    employee_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        model = ProfessionalInfo
        fields = ['employee_id', 'first_name', 'last_name', 'phone_number', 'pan_card_number', 'position', 'salary', 'perks']
