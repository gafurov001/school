from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from users.models import User
from users.serializers import UserModelSerializer, UserCreateModelSerializer, UserRetrieveUpdateDestroyModelSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateDestroyModelSerializer
