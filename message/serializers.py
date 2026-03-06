from rest_framework import serializers
from .models import Message,UserAnalytics
from django.contrib.auth.models import User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta :
        model = User
        fields = ['username' , 'email' , 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = "user.username")
    class Meta:
        model = Message
        fields = ['url','id','user' , 'message']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    messages = serializers.HyperlinkedRelatedField(
        many = True, view_name = 'messages-detail', read_only = True, lookup_field = 'pk'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="user-detail"
    )
    class Meta:
        model = User
        fields = ['url','username' , 'id' , 'messages']
from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        user = authenticate(
            username=data["username"],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        data["user"] = user
        return data