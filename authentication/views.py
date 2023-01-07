from rest_framework.generics import GenericAPIView
from authentication.serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

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