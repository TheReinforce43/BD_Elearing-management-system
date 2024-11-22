from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView
)


# Import all related models 
from django.contrib.auth.models import Group 

# Import all related serializer 

from User.Serializer.group_serializer import  (
    CreateGroupSerializer, 
    GetGroupSerializer
)

class CreateGroupAPI(CreateAPIView):
    serializer_class = CreateGroupSerializer
    queryset = Group.objects.all()


class GetGroupAPIView(ListAPIView):
    serializer_class = GetGroupSerializer
    queryset = Group.objects.all()


class UpdateGroupAPI(UpdateAPIView):
    serializer_class = CreateGroupSerializer
    queryset = Group.objects.all()


class RetrieveDestroyAPI(RetrieveDestroyAPIView):
    serializer_class = GetGroupSerializer
    queryset = Group.objects.all()