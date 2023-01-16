from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from api.serializer import CategorySerializer,TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from api.models import Category,ToDo
from rest_framework.parsers import MultiPartParser
import cloudinary.uploader
from django.shortcuts import get_object_or_404
from authentication.models import User
from rest_framework.views import APIView


def userExists(id):
    # Function to check if a user with the given id exists in the database
    
    if User.objects.filter(id=id).exists():
        # Checking if a user with the given id exists in the database
        return True
    return False
# call that class on root url
class WebApplicationMessage(CreateAPIView):
    authentication_classes=[]
    serializer_class=CategorySerializer
    def get(self, request):
        responseData = {
        "message": "Yes, Backend DRF is running!",
        "meta-data":{"meta":"developed for TaskHelper Frontend",
        "status":status.HTTP_200_OK}
        }
        return JsonResponse(responseData)

class CategoryAPIView(CreateAPIView):
    # View class for handling the creation of categories
    
    serializer_class=CategorySerializer
    # Setting the serializer class for the view to the CategorySerializer class
    
    permission_classes=(IsAuthenticated,)
    # Setting the permission class for the view to IsAuthenticated, meaning only authenticated users can access this view
    
    def get(self,request):
        # Handling GET requests to the view
        
        tasks=Category.objects.all()
        # Retrieving all categories from the database
        
        serializer=self.serializer_class(tasks,many=True)
        # Initializing the serializer with the retrieved categories and setting the many parameter to True
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        # Returning the serialized data with a status of 200 OK
    
    def post(self,request,format=None):
        # Handling POST requests to the view
        
        serializer=self.serializer_class(data=request.data)
        # Initializing the serializer with the data from the request
        
        if serializer.is_valid():
            # Checking if the serializer is valid
            
            serializer.save()
            # Saving the serializer
            
            return Response({"message":"Category is created sucessfully!"},status=status.HTTP_201_CREATED)
            # Returning a message and a status of 201 CREATED
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        # Returning the serializer errors and a status of 400 BAD REQUEST if the serializer is not valid

class TodoAPIView(CreateAPIView):
    # View class for handling the creation of ToDo items
    
    serializer_class=TodoSerializer
    # Setting the serializer class for the view to the TodoSerializer class
    
    permission_classes=(IsAuthenticated,)
    # Setting the permission class for the view to IsAuthenticated, meaning only authenticated users can access this view
    
    parser_classes = (MultiPartParser,)
    # Setting the parser class for handling image file
    
    queryset = ToDo.objects.all()
    # Setting the queryset for the view to all ToDo objects
    
    serializer_class = TodoSerializer
    # Setting the serializer class for the view to the TodoSerializer class
    
    def get(self,request):
        # Handling GET requests to the view
        
        tasks=ToDo.objects.all()
        # Retrieving all ToDo items from the database
        
        serializer=self.serializer_class(tasks,many=True)
        # Initializing the serializer with the retrieved ToDo items and setting the many parameter to True
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        # Returning the serialized data with a status of 200 OK
        
    def post(self, request, format=None):
        # Handling POST requests to the view

        serializer = self.serializer_class(data=request.data)
        # Initializing the serializer with the data from the request
        
        if serializer.is_valid():
            # Checking if the serializer is valid
            
            image=request.FILES.get('image',None)
            # Getting the image file from the request, if any
            
            if image:
                # If an image file was included in the request
                image_url = cloudinary.uploader.upload(request.data['image'])['url']
                # uploading the image file to cloudinary and getting the url
                serializer.validated_data['image'] = image_url
                # Adding the image url to the validated data of the serializer
                
            serializer.save()
            # Saving the serializer
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # Returning the serialized data with a status of 201 CREATED
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Returning the serializer errors and a status of 400 BAD REQUEST if the serializer is not valid


class CategorySpecificAPIView(CreateAPIView):
    # View class for handling the CRUD operations for a specific category based on its id

    serializer_class=CategorySerializer
    # Setting the serializer class for the view to the CategorySerializer class
    
    permission_classes=(IsAuthenticated,)
    # Setting the permission class for the view to IsAuthenticated, meaning only authenticated users can access this view

    def get(self,request,pk):
        # Handling GET requests to the view

        if Category.objects.filter(id=pk).exists():
            # Checking if a category with the given id exists in the database
            
            category=Category.objects.get(id=pk)
            # Retrieving the category from the database
            
            serializer=self.serializer_class(category,many=False)
            # Initializing the serializer with the retrieved category and setting the many parameter to False
            
            return Response(serializer.data,status=status.HTTP_200_OK)
            # Returning the serialized data with a status of 200 OK
        else:
            return Response({"message":"Category not found!"},status=status.HTTP_404_NOT_FOUND)
            # Returning a message and a status of 404 NOT FOUND if the category does not exist in the database

    def put(self,request,pk):
        # Handling PUT requests to the view
        
        if Category.objects.filter(id=pk).exists():
            # Checking if a category with the given id exists in the database
            
            category=Category.objects.get(id=pk)
            # Retrieving the category from the database
            
            serializer=self.serializer_class(instance=category,data=request.data)
            # Initializing the serializer with the retrieved category and the data from the request
            
            if serializer.is_valid():
                # Checking if the serializer is valid
                
                serializer.save()
                # Saving the serializer
                
                return Response(serializer.data,status=status.HTTP_200_OK)
                # Returning the serialized data with a status of 200 OK
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # Returning the serializer errors and a status of 400 BAD REQUEST if the serializer is not valid
        else:
            return Response({"message":"Category not found!"},status=status.HTTP_404_NOT_FOUND)
            # Returning a message and a status of 404 NOT FOUND if the category does not exist in the database

    def delete(self,request,pk):
        # Handling DELETE requests to the view
        
        if Category.objects.filter(id=pk).exists():
            # Checking if a category with the given id exists in the database
            
            category=Category.objects.get(id=pk)
            # Retrieving the category from the database
            
            category.delete()
            # Deleting the category from the database
            
            return Response({"message":"Category is deleted sucessfully!"},status=status.HTTP_200_OK)
            # Returning a message and a status of 200 OK
        else:
            return Response({"message":"Category not found!"},status=status.HTTP_404_NOT_FOUND)


class TodoSpecifcAPIView(CreateAPIView):
    # View class for handling the CRUD operations for a specific ToDo item based on its id

    serializer_class=TodoSerializer
    # Setting the serializer class for the view to the TodoSerializer class
    
    permission_classes=(IsAuthenticated,)
    # Setting the permission class for the view to IsAuthenticated, meaning only authenticated users can access this view

    def get(self,request,pk):
        # Handling GET requests to the view

        if ToDo.objects.filter(id=pk).exists():
            # Checking if a ToDo item with the given id exists in the database
            
            tasks=ToDo.objects.get(id=pk)
            # Retrieving the ToDo item from the database
            
            serializer=self.serializer_class(tasks,many=False)
            # Initializing the serializer with the retrieved ToDo item and setting the many parameter to False
            
            return Response(serializer.data,status=status.HTTP_200_OK)
            # Returning the serialized data with a status of 200 OK
        else:
            return Response({"message":"Todo not found!"},status=status.HTTP_404_NOT_FOUND)
            # Returning a message and a status of 404 NOT FOUND if the ToDo item does not exist in the database

    def put(self, request, pk, format=None):
        # Handling PUT requests
        todo = get_object_or_404(ToDo, pk=pk)
        # Retrieving the ToDo item with the given id, or returning a 404 error if it doesn't exist
        
        serializer = self.serializer_class(todo, data=request.data)
        # Initializing the serializer with the retrieved ToDo item and the data from the request
        
        if serializer.is_valid():
            # Checking if the serializer is valid
            
            if 'image' in request.data:
                # Checking if the request data includes an image file
                
                image=request.FILES.get('image',None)
                # Getting the image file from the request
                
                image_url = cloudinary.uploader.upload(image)['url']
                # uploading the image file to cloudinary and getting the url
                
                serializer.validated_data['image'] = image_url
                # Adding the image url to the validated data of the serializer
                
            else:
                print("Image is not in request")
                # Printing a message if the request data does not include an image file
                
            serializer.save()
            # Saving the serializer
            
            return Response(serializer.data)
            # Returning the serialized data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Returning the serializer errors and a status of 400 BAD REQUEST if the serializer is not valid

    def delete(self,request,pk):
        # Handling DELETE requests to the view
        
        if ToDo.objects.filter(id=pk).exists():
            # Checking if a ToDo item with the given id exists in the database
            
            todo=ToDo.objects.get(id=pk)
            # Retrieving the ToDo item from the database
            
            todo.delete()
            # Deleting the ToDo item from the database
            
            return Response("Todo is deleted sucessfully!",status=status.HTTP_200_OK)
            # Returning a message and a status of 200 OK
        else:
            return Response({"message":"Todo will this id doesn't exists!"},status=status.HTTP_400_BAD_REQUEST)
            # Returning a message and a status of 400 BAD REQUEST if the ToDo item does not exist in the database


class CategoryUserSpecifcAPIView(CreateAPIView):
    # View class for handling the CRUD operations for a specific user's categories
    
    serializer_class=CategorySerializer
    # Setting the serializer class for the view to the CategorySerializer class
    
    permission_classes=(IsAuthenticated,)
    # Setting the permission class for the view to IsAuthenticated, meaning only authenticated users can access this view
    
    def get(self,request):
        # Handling GET requests to the view
        
        if(userExists(request.user.id)):
            # Checking if the user exists using the userExists function
            
            category=Category.objects.filter(user=request.user.id)
            # Retrieving all the categories for the user from the database
            
            serializer=self.serializer_class(instance=category,many=True)
            # Initializing the serializer with the retrieved categories and setting the many parameter to True
            
            if(len(serializer.data)<1):
                return Response({"message":"User dont have any category"},status=status.HTTP_200_OK)    
                # Returning a message with a status of 200 OK if the user does
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"User not exists"},status=status.HTTP_404_NOT_FOUND)

class TodoUserSpecifcAPIView(CreateAPIView):
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        if(userExists(request.user.id)):
            userID=request.GET['userID']
            todo=ToDo.objects.filter(user=userID)
            serializer=self.serializer_class(instance=todo,many=True)
            if(len(serializer.data)<1):
                return Response({"message":"User dont have any todo"},status=status.HTTP_404_NOT_FOUND)    
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"User not exists"},status=status.HTTP_404_NOT_FOUND)

class CategoryCurrentUserAPIView(CreateAPIView):
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        # Check if the user exists
        if(userExists(request.user.id)):
            # Retrieve all categories associated with the current user
            category=Category.objects.filter(user=request.user.id)
            # Initialize serializer with the retrieved categories and set many=True since there are multiple categories
            serializer=self.serializer_class(instance=category,many=True)
            # Check if the user has any categories
            if(len(serializer.data)<1):
                # If the user doesn't have any categories, return a message saying so
                return Response({"message":"User dont have any category"},status=status.HTTP_200_OK)    
            # Otherwise, return the serialized data
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            # If the user does not exist, return a message saying so
            return Response({"message":"User not exists"},status=status.HTTP_404_NOT_FOUND)


class ToDoCurrentUserAPIView(CreateAPIView):
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        # Check if the user exists
        if(userExists(request.user.id)):
            # Retrieve all Todos associated with the current user
            Todo=ToDo.objects.filter(user=request.user.id)
            # Initialize serializer with the retrieved Todos and set many=True since there are multiple Todos
            serializer=self.serializer_class(instance=Todo,many=True)
            # Check if the user has any Todos
            if(len(serializer.data)<1):
                # If the user doesn't have any Todos, return a message saying so
                return Response({"message":"User dont have any Todo"},status=status.HTTP_200_OK)    
            # Otherwise, return the serialized data
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            # If the user does not exist, return a message saying so
            return Response({"message":"User not exists"},status=status.HTTP_404_NOT_FOUND)


class ToDoCurrentUserDeleteAPIView(CreateAPIView):
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    queryset = ToDo.objects.all()

    def delete(self, request):
        # Check if the user exists
        if(userExists(request.user.id)):
            # Get the current user
            user = request.user
            # Retrieve all the tasks associated with the current user
            tasks = ToDo.objects.filter(user=user)
            # Delete all the tasks
            tasks.delete()
            # Return a message indicating that all tasks were deleted successfully
            return Response({"message":"All tasks are deleted successfully!"},status=status.HTTP_200_OK)
        else:
            # If the user does not exist, return a message saying so
            return Response({"message":"User not exists"},status=status.HTTP_404_NOT_FOUND)


class CategoryCurrentUserDeleteAPIView(CreateAPIView):
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,)
    queryset = Category.objects.all()

    def delete(self, request):
        # Check if the user exists
        if(userExists(request.user.id)):
            # Get the current user
            user = request.user
            # Retrieve all the categories associated with the current user
            category = Category.objects.filter(user=user)
            # Delete all the categories
            category.delete()
            # Return a message indicating that all categories were deleted successfully
            return Response({"message":"All categories are deleted successfully!"},status=status.HTTP_200_OK)
        else:
            # If the user does not exist, return a message saying so
            return Response({"message":"User not exists"},status=status.HTTP_404_NOT_FOUND)
