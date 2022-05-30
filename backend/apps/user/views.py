from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import AnilistModel, KitsuModel, MalModel
from .serializers import (
    AnilistSerializer,
    KitsuSerializer,
    MalSerializer,
    UserSerializer,
)

# Create your views here.


class UserInfoView(generics.ListCreateAPIView):
    """
    ⦿  Shows User Info.
    ⦿  Accpets User Info changes.
    """

    serializer_class = UserSerializer
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]
    parser_classes = [
        FormParser,
        MultiPartParser,
    ]

    def get(self, request: HttpRequest) -> Response:
        data = get_user_model().objects.get(id=request.user.id)
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)

    def post(self, request: HttpRequest) -> Response:
        instance = get_user_model().objects.get(id=request.user.id)
        serializer = self.get_serializer(data=request.data, instance=instance)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    """
    ⦿ User Registration Endpoint
    """

    serializer_class = UserSerializer
    parser_classes = [
        FormParser,
        MultiPartParser,
    ]
    permission_classes = [
        AllowAny,
    ]

    def post(self, request: HttpRequest) -> Response:
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MalView(generics.ListCreateAPIView):
    """"""

    serializer_class = MalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = MalModel.objects.filter(user=self.request.user)
        return queryset


class KitsuView(generics.ListCreateAPIView):
    """"""

    serializer_class = KitsuSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        queryset = KitsuModel.objects.filter(user=self.request.user)
        return queryset


class AnilistView(generics.ListCreateAPIView):
    """"""

    serializer_class = AnilistSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        queryset = AnilistModel.objects.filter(user=self.request.user)
        return queryset
