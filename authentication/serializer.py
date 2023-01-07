from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=125,min_length=6,write_only=True)
    class Meta:
        model=User
        fields=("username","email","password","id")
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)