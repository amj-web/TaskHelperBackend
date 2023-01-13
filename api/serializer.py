from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import ToDo,Category
from authentication.models import User

class CategorySerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model=Category
        fields=('id','name','user')
class TodoSerializer(ModelSerializer):
    image = serializers.CharField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model=ToDo
        fields=('id','title','description','assigned','dueDate','image','status','priority','user','category')