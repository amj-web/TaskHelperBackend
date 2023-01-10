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
    authentication_classes=[]
    serializer_class=LoginSerializer

    def post(self,request):
        email=request.data.get('email',None)
        password=request.data.get('password',None)

        user=authenticate(username=email,password=password)
        if user:
            serializer=self.serializer_class(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message':"Invalid credentials, try again"},status=status.HTTP_401_UNAUTHORIZED)
        
class AuthUserAPIView(GenericAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class=RegisterSerializer

    def get(self,request):
        user=request.user
        serializer=self.serializer_class(user)
        return Response({'message':serializer.data},status=status.HTTP_200_OK)

class UserAPIView(GenericAPIView):
    serializer_class=UserSerializer
    def get(self,request):
        user=User.objects.all()
        serializer=self.serializer_class(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserSpecificAPIView(GenericAPIView):
    authentication_classes=[]
    serializer_class=UserSerializer
    def get(self,request,id):
        if(userExists(id)):
            user=User.objects.get(id=id)
            serializer=self.serializer_class(instance=user)                
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"User with this id doesn't exists!"},status=status.HTTP_200_OK)