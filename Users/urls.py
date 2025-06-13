from django.urls import path
from .views import UserList, FollowCreate

urlpatterns = [
    path('users/', UserList.as_view()),
    path('follows/', FollowCreate.as_view()),
]
