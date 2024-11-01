from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, CharField, DateField, Model, ImageField, \
    IntegerField

from users.managers import CustomUserManager


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        TEACHER = 'teacher', 'Teacher'

    username = None
    role = CharField(max_length=20, choices=Role.choices)
    phone_number = CharField(max_length=13, unique=True)
    branch = CharField(max_length=255)
    date_of_birth = DateField()
    gender = CharField(choices=[('male', 'Male'), ('female', 'Female')])
    balance = IntegerField(null=True, blank=True)
    photo = ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()



