import jwt
from rest_framework import authentication, exceptions
from django.conf import settings

from api.models import User


class JWTAuthenticationProvider(authentication.BaseAuthentication):
    """
    This module is used to provide all the basic actions related to
    JWT authentication in the application as required by DRF.
    """
    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request)

        if not auth_header:
            return None

        prefix, auth_token = auth_header.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(auth_token, settings.SECRET_KEY, 'HS256')
            user = User.objects.get(phone_number=payload['phone_number'])
            return user, auth_token
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('You are unauthorized.')
        except jwt.ExpiredSignatureError:
            """
            In this case we can build an refresh token guided auth_token issuing process on the client part.
            """
            raise exceptions.AuthenticationFailed('Your authorization has expired. Please login again.')
        return super().authenticate(request)