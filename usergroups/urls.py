
from django.urls import path, include
from . import views

urlpatterns = [
     path('groups/', views.UserGroupList.as_view(), name='user_group_list'),
    path('groups/<int:pk>',
        views.UserGroupDetail.as_view(), name='user_group_detail'),
]