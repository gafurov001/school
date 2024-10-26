from rest_framework.serializers import ModelSerializer

from group.models import Group, SkippedClass, Room


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
        fields = 'name', 'room_capacity', 'number_of_desks_and_chairs'
