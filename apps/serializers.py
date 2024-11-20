from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Group, SkippedClass, Room, User, Course


class GroupModelSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = 'id', 'name', 'teacher', 'course_start_time', 'day'

    def to_representation(self, instance):
        return super().to_representation(instance)


class GroupCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = 'name', 'teacher', 'day', 'room', 'course_start_time'


class SkippedClassModelSerializer(ModelSerializer):
    class Meta:
        model = SkippedClass
        fields = 'student', 'group'


class RoomModelSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class StudentModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'phone_number'


class StudentCreateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'phone_number', 'password', 'date_of_birth', 'gender', 'photo'


class StudentRetrieveUpdateDestroyModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'phone_number', 'balance', 'branch', 'date_of_birth', 'gender', 'photo'


class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'phone_number', 'role', 'photo', 'date_of_birth', 'gender'


class WorkerCreateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'phone_number', 'role', 'date_of_birth', 'gender', 'photo'


class WorkerRetrieveUpdateDestroyModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
