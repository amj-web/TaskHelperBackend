from rest_framework.generics import CreateAPIView
from api.serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from api.models import Category

# Create your views here.
class CategoryAPIView(CreateAPIView):
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        tasks=Category.objects.all()
        serializer=self.serializer_class(tasks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Category is created sucessfully!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
