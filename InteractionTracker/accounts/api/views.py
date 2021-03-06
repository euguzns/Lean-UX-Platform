"""
 # Interaction Tracker
 # @license http://www.apache.org/licenses/LICENSE-2.0
 # Author @ Jamil Hussain, Zaki
"""


from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from accounts.models import (MyUser)


from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserListSerializer
    )

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = MyUser.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserListAPIview(ListAPIView):
        queryset = MyUser.objects.all()
        serializer_class = UserListSerializer




















