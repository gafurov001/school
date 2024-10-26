from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView

from group.models import Group, SkippedClass, Room
from group.serializers import GroupModelSerializer, GroupCreateModelSerializer, SkippedClassModelSerializer, \
    RoomModelSerializer


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
