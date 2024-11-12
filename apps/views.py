from django.contrib.auth.hashers import make_password
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    GenericAPIView

from apps.models import Group, SkippedClass, Room, User, Course
from apps.serializers import GroupModelSerializer, GroupCreateModelSerializer, SkippedClassModelSerializer, \
    RoomModelSerializer, StudentModelSerializer, StudentCreateModelSerializer, \
    StudentRetrieveUpdateDestroyModelSerializer, \
    CourseModelSerializer, WorkerRetrieveUpdateDestroyModelSerializer, WorkerCreateModelSerializer, \
    WorkerModelSerializer


class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateModelSerializer


class GroupRetrieveAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateModelSerializer


class GroupDestroyAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateModelSerializer


class GroupUpdateAPIView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateModelSerializer


class SkippedClassListAPIView(ListAPIView):
    queryset = SkippedClass.objects.all()
    serializer_class = SkippedClassModelSerializer


class SkippedClassCreateAPIView(CreateAPIView):
    queryset = SkippedClass.objects.all()
    serializer_class = SkippedClassModelSerializer


class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class RoomDestroyAPIView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class StudentListAPIView(ListAPIView):
    queryset = User.objects.filter(role='student').all()
    serializer_class = StudentModelSerializer


class StudentCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentCreateModelSerializer

    def create(self, request, *args, **kwargs):
        request.data['role'] = 'student'
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)


class StudentDestroyAPIView(DestroyAPIView):
    queryset = User.objects.filter(role='student').all()
    serializer_class = StudentRetrieveUpdateDestroyModelSerializer


class StudentGenericAPIView(GenericAPIView):
    queryset = User.objects.filter(role='student').all()
    serializer_class = StudentRetrieveUpdateDestroyModelSerializer

    def post(self, request, pk):
        return User.objects.filter(id=pk).update(**request.data)


class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.filter(role='student').all()
    serializer_class = StudentRetrieveUpdateDestroyModelSerializer


class WorkerListAPIView(ListAPIView):
    queryset = User.objects.filter(role__in=['admin', 'moderator', 'teacher']).all()
    serializer_class = WorkerModelSerializer


class WorkerCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = WorkerCreateModelSerializer


class WorkerDestroyAPIView(DestroyAPIView):
    queryset = User.objects.filter(role__in=['admin', 'moderator', 'teacher']).all()
    serializer_class = WorkerRetrieveUpdateDestroyModelSerializer


class WorkerGenericAPIView(GenericAPIView):
    queryset = User.objects.filter(role__in=['admin', 'moderator', 'teacher']).all()
    serializer_class = WorkerRetrieveUpdateDestroyModelSerializer

    def post(self, request, pk):
        return User.objects.filter(id=pk).update(**request.data)


class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.filter(role__in=['admin', 'moderator', 'teacher']).all()
    serializer_class = WorkerRetrieveUpdateDestroyModelSerializer


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
