from django.urls import path ,include


from User.API.group_api import (
    CreateGroupAPI,
    GetGroupAPIView,
    UpdateGroupAPI,
    RetrieveDestroyAPI
)

urlpatterns = [
    path('add/',CreateGroupAPI.as_view(),name='create_list_group'),
    path('list/',GetGroupAPIView.as_view(),name='create_list_group'),
    path('update/<int:pk>',UpdateGroupAPI.as_view(),name='update_list_group'),
    path('retrieve/<int:pk>',RetrieveDestroyAPI.as_view(),name='update_list_group'),
    path('delete/<int:pk>',RetrieveDestroyAPI.as_view(),name='update_list_group'),

]
