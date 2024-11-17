from django.contrib.auth.models import AbstractUser
from django.db.models import Model, SET_NULL, TextChoices, CharField, ForeignKey, DateField, TimeField, \
    IntegerField, CASCADE, TextField, ImageField, BooleanField

from apps.managers import CustomUserManager


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    username = None
    role = CharField(max_length=20, choices=Role.choices)
    phone_number = CharField(max_length=13, unique=True)
    branch = CharField(max_length=255)
    photo = TextField(null=True, blank=True)
    date_of_birth = DateField()
    gender = CharField(choices=[('male', 'Male'), ('female', 'Female')])
    balance = IntegerField(null=True, blank=True)
    date_joined = None
    is_active = BooleanField(default=True)
    is_staff = None
    is_superuser = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Room(Model):
    name = CharField(max_length=20)
    room_capacity = CharField(max_length=10)
    number_of_desks_and_chairs = CharField(max_length=20)


class Group(Model):
    class Days(TextChoices):
        HAR_KUN = 'har kun', 'har kun'
        JUFT_KUN = 'juft kun', 'Juft'
        TOQ_KUN = 'toq kun', 'Toq kun'

    name = CharField(max_length=50)
    teacher = ForeignKey('User', SET_NULL, null=True, blank=True)
    day = CharField(max_length=20, choices=Days.choices)
    room = ForeignKey('Room', SET_NULL, null=True, blank=True)
    course_start_date = DateField(null=True, blank=True)
    course_end_date = DateField(null=True, blank=True)
    course_start_time = TimeField()
    course = ForeignKey('Course', SET_NULL, null=True, blank=True)


class SkippedClass(Model):
    student = ForeignKey('User', CASCADE)
    group = ForeignKey('Group', CASCADE)
    date = DateField(auto_now=True)


class Debtor(Model):
    student = ForeignKey('User', CASCADE)
    comment = TextField(null=True, blank=True)


class Course(Model):
    class Type(TextChoices):
        ONLINE = 'online', 'Online'
        OFFLINE = 'offline', 'Offline'
        VIDEO_COURSE = 'video course', 'Video course'

    name = CharField(max_length=30)
    type = CharField(max_length=20, choices=Type.choices)
    price = IntegerField()
    comment = TextField()
