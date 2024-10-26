from rest_framework.serializers import ModelSerializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'phone_number', 'role'


class UserCreateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'phone_number', 'role', 'date_of_birth', 'gender', 'photo'


class UserRetrieveUpdateDestroyModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'photo', 'balance', 'role', 'branch'
