import datetime

import jwt
import pytz
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers.UserLoginSerializer import UserLoginSerializer


class UserLoginView(GenericAPIView):
    """
    This endpoint is only responsible to handle Login request into this application.
    """
    serializer_class = UserLoginSerializer

    def post(self, request):
        phone_number = request.data.get('phone_number', '')
        password = request.data.get('password', '')
        user = auth.authenticate(phone_number=phone_number, password=password)

        if user is not None:
            serializer = UserLoginSerializer(user)
            token_payload = {
                "phone_number": phone_number,
                "exp": datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE)) + datetime.timedelta(days=60)
            }
            auth_token = jwt.encode(token_payload, settings.SECRET_KEY, 'HS256')
            response_data = {
                'user': serializer.data,
                'auth_token': auth_token
            }
            return Response(data=response_data, status=status.HTTP_200_OK)
        return Response(
            data={'error': 'Invalid Login Credentials. Please try again.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
