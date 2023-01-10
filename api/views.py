from rest_framework.generics import CreateAPIView
from api.serializer import CategorySerializer,TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from api.models import Category,ToDo
from rest_framework.parsers import MultiPartParser
import cloudinary.uploader
from django.shortcuts import get_object_or_404

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

class CategorySpecificAPIView(CreateAPIView):
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,)

    def get(self,request,pk):
        if Category.objects.filter(id=pk).exists():
            category=Category.objects.get(id=pk)
            serializer=self.serializer_class(category,many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Category not found!"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        if Category.objects.filter(id=pk).exists():
            category=Category.objects.get(id=pk)
            serializer=self.serializer_class(instance=category,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Category not found!"},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Category.objects.filter(id=pk).exists():
            category=Category.objects.get(id=pk)
            category.delete()
            return Response({"message":"Category is deleted sucessfully!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Category not found!"},status=status.HTTP_404_NOT_FOUND)


class TodoSpecifcAPIView(CreateAPIView):
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    def get(self,request,pk):
        if ToDo.objects.filter(id=pk).exists():
            tasks=ToDo.objects.get(id=pk)
            serializer=self.serializer_class(tasks,many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Todo not found!"},status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk, format=None):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = self.serializer_class(todo, data=request.data)
        if serializer.is_valid():
            if 'image' in request.data:
                print("Image is in request")
                image=request.FILES.get('image',None)
                image_url = cloudinary.uploader.upload(image)['url']
                serializer.validated_data['image'] = image_url
            else:
                print("Image is not in request")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        if ToDo.objects.filter(id=pk).exists():
            todo=ToDo.objects.get(id=pk)
            todo.delete()
            return Response("Todo is deleted sucessfully!",status=status.HTTP_200_OK)
        else:
            return Response({"message":"Todo will this id doesn't exists!"},status=status.HTTP_400_BAD_REQUEST)
