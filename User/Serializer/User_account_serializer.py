from rest_framework import serializers 
from User.models import User



class UserSignUpSerializer(serializers.ModelSerializer):


    class Meta:
        model = User 
        fields='__all__'
