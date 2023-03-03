from rest_framework import serializers
from authentication.models import User

# converting objects into data types understandable by ReactJs


# Register serializer willhandle data regarding user registrations
class RegisterSerializer(serializers.ModelSerializer):
    password = (serializers.CharField(max_length=125,
                                      min_length=6, write_only=True))

    class Meta:
        model = User
        fields = ("username", "email", "password", "id")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# Login serializer willhandle data regarding user login
class LoginSerializer(serializers.ModelSerializer):
    password = (serializers.CharField(max_length=125,
                                      min_length=6, write_only=True))

    class Meta:
        model = User
        fields = ("username", "email", "password", "token", "id")
        read_only_fields = ["token"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "id")
