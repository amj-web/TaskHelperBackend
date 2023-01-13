from rest_framework.authentication import get_authorization_header,BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from authentication.models import User

class JWTAuthentication(BaseAuthentication):

    def authenticate(self,request):
        # Get the authorization header from the request
        auth_header=get_authorization_header(request)
        auth_data=auth_header.decode('utf-8')
        auth_token=auth_data.split(" ")
        # Check if the token is in the correct format
        if len(auth_token)!=2:
            # If the token is not in the correct format, raise an exception
            raise exceptions.AuthenticationFailed('Token is not valid!')
        token=auth_token[1]
        try:
            # Decode the token using the secret key
            payload=jwt.decode(token,settings.SECRET_KEY,algorithms='HS256')
            # Get the username from the payload
            username=payload['username']
            # Get the user from the database using the username
            user=User.objects.get(username=username)
            # Return the user and token
            return (user,token)

        except jwt.ExpiredSignatureError as ex:
            # If the token is expired, raise an exception
            raise exceptions.AuthenticationFailed("Token is expired, please login again")

        except jwt.DecodeError as ex:
            # If the token is invalid, raise an exception
            raise exceptions.AuthenticationFailed("Token is invalid")

        except User.DoesNotExist as ex:
            # If the user does not exist, raise an exception
            raise exceptions.AuthenticationFailed("No such user exist")

        return super().authenticate(request)
