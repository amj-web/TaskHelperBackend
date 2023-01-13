from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import ToDo,Category
from authentication.models import User

# Importing required libraries and modules

class CategorySerializer(ModelSerializer):
    # Serializer for the Category model
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # Defining the user field as a PrimaryKeyRelatedField and setting the queryset to all User objects
    
    class Meta:
        model=Category
        # Setting the model for the serializer to the Category model
        
        fields=('id','name','user')
        # Specifying which fields of the model should be included in the serialized output

class TodoSerializer(ModelSerializer):
    # Serializer for the ToDo model
    
    image = serializers.CharField(read_only=True)
    # Defining the image field as a CharField and setting it as read-only
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # Defining the user field as a PrimaryKeyRelatedField and setting the queryset to all User objects
    
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # Defining the category field as a PrimaryKeyRelatedField and setting the queryset to all Category objects
    
    class Meta:
        model=ToDo
        # Setting the model for the serializer to the ToDo model
        
        fields=('id','title','description','assigned','dueDate','image','status','priority','user','category')
        # Specifying which fields of the model should be included in the serialized output
