from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.models import Group, SkippedClass, Room, User, Course
from apps.serializers import GroupModelSerializer, GroupCreateModelSerializer, SkippedClassModelSerializer, \
    RoomModelSerializer, UserModelSerializer, UserCreateModelSerializer, UserRetrieveUpdateDestroyModelSerializer, \
    CourseModelSerializer


class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateModelSerializer


class SkippedClassListCreateAPIView(ListCreateAPIView):
    queryset = SkippedClass.objects.all()
    serializer_class = SkippedClassModelSerializer


class RoomListCreateAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateDestroyModelSerializer


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
