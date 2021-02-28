from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers.UserAccountSerializer import UserAccountSerializer


class UserAccountView(GenericAPIView):
    """
    This view shall be used to create new records in the User model through POST request
    """
    serializer_class = UserAccountSerializer

    def post(self, request):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
