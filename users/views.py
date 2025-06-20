from rest_framework import generics
from .models import UserProfile
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
