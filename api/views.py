from rest_framework.generics import CreateAPIView
from api.serializer import CategorySerializer,TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from api.models import Category,ToDo
from rest_framework.parsers import MultiPartParser
import cloudinary.uploader

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

class TodoAPIView(CreateAPIView):
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    def get(self,request):
        tasks=ToDo.objects.all()
        serializer=self.serializer_class(tasks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image=request.FILES.get('image',None)
            if image:
                image_url = cloudinary.uploader.upload(request.data['image'])['url']
                serializer.validated_data['image'] = image_url
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

