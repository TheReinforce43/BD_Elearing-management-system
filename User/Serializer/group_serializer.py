from rest_framework import serializers 
from django.contrib.auth.models import  Group ,Permission


# Import all related serializers 

from User.Serializer.permission_serializer import PermissionSerializer 


class CreateGroupSerializer(serializers.ModelSerializer):
    permissions= serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(),many=True)

    class Meta:
        model = Group
        fields = '__all__'



class GetGroupSerializer(serializers.ModelSerializer):
    permissions= PermissionSerializer(read_only=True,many=True) 
    class Meta:
        model = Group
        fields = '__all__'