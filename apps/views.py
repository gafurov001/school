from django.contrib.auth.hashers import make_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, \
    GenericAPIView
from rest_framework.response import Response

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


class GroupGenericAPIView(GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateModelSerializer

    def post(self, request, pk):
        group = Group.objects.filter(id=pk).update(**request.data)
        return Response(status=201)


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

class RoomRetrieveAPIView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class RoomGenericAPIView(GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer

    def post(self, request, pk):
        room = Room.objects.filter(id=pk).update(**request.data)
        return Response(status=201)


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
        user = User.objects.filter(id=pk).update(**request.data)
        return Response(status=201)


class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.filter(role='student').all()
    serializer_class = StudentRetrieveUpdateDestroyModelSerializer


class WorkerListAPIView(ListAPIView):
    queryset = User.objects.filter(role__in=['admin', 'moderator', 'teacher']).all()
    serializer_class = WorkerModelSerializer
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'role',


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
        user = User.objects.filter(id=pk).update(**request.data)
        return Response(status=201)


class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.filter(role__in=['admin', 'moderator', 'teacher']).all()
    serializer_class = WorkerRetrieveUpdateDestroyModelSerializer


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


class StudentCountGenericAPIView(GenericAPIView):
    queryset = User.objects.filter(role='student').all()

    def get(self, request):
        _count = User.objects.filter(role='student').count()
        return Response({"count": _count})


class GroupCountGenericAPIView(GenericAPIView):
    queryset = Group.objects.all()

    def get(self, request):
        _count = Group.objects.count()
        return Response({"count": _count})


class WorkerCountGenericAPIView(GenericAPIView):
    queryset = User.objects.filter(role__in=['admin', 'teacher', 'moderator']).all()

    def get(self, request):
        _count = User.objects.filter(role__in=['admin', 'teacher', 'moderator']).count()
        return Response({"count": _count})


class RoomCountGenericAPIView(GenericAPIView):
    queryset = Room.objects.all()

    def get(self, request):
        _count = Room.objects.count()
        return Response({"count": _count})




