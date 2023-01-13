from rest_framework.generics import GenericAPIView
from authentication.serializer import RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status,permissions
from django.contrib.auth import authenticate
from authentication.models import User

def userExists(id):
    if User.objects.filter(id=id).exists():
        return True
    return False


# This will responsible for registering the users
class RegisterAPIView(GenericAPIView):
    # no need for authentication for registration
    authentication_classes=[] 
    # we will use our RegisterSerializer for parsing
    serializer_class=RegisterSerializer
    
    def post(self,request):
        # send all data to our serializer
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(): #if everything is valid than save
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    # no authentication classes are used
    authentication_classes=[]
    serializer_class=LoginSerializer

    def post(self,request):
        # get email and password from request data
        email=request.data.get('email',None)
        password=request.data.get('password',None)

        # authenticate the user using email and password
        user=authenticate(username=email,password=password)
        if user:
            # create a serializer with the user
            serializer=self.serializer_class(user)
            # return the serialized data and status 200
            return Response(serializer.data,status=status.HTTP_200_OK)
        # if user not found, return response with message 'Invalid credentials, try again' and status 401
        return Response({'message':"Invalid credentials, try again"},status=status.HTTP_401_UNAUTHORIZED)

        
class AuthUserAPIView(GenericAPIView):
    # only authenticated user can access this view
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class=RegisterSerializer

    def get(self,request):
        # Get the current authenticated user
        user=request.user
        # Initialize the serializer with the user
        serializer=self.serializer_class(user)
        # Return the serialized data and status 200
        return Response({'message':serializer.data},status=status.HTTP_200_OK)

class UserAPIView(GenericAPIView):
    serializer_class=UserSerializer
    def get(self,request):
        # Get all the users from the database
        user=User.objects.all()
        # Initialize the serializer with the users and set many=True since there are multiple users
        serializer=self.serializer_class(user,many=True)
        # Return the serialized data and status 200
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserSpecificAPIView(GenericAPIView):
    authentication_classes=[]
    serializer_class=UserSerializer
    def get(self,request,id):
        # check if user exists with given id
        if(userExists(id)):
            # get user from database with the given id
            user=User.objects.get(id=id)
            # initialize serializer with user
            serializer=self.serializer_class(instance=user)                
            # return the serialized data and status 200
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            # if user not found, return response with message 'User with this id doesn't exists!' and status 200
            return Response({"message":"User with this id doesn't exists!"},status=status.HTTP_200_OK)
