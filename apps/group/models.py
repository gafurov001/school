from django.db.models import Model, OneToOneField, SET_NULL, TextChoices, CharField, ForeignKey, DateField, TimeField, \
    IntegerField, CASCADE, TextField


class Room(Model):
    name = CharField(max_length=20)
    room_capacity = CharField(max_length=10)
    number_of_desks_and_chairs = CharField(max_length=20)


class Group(Model):
    class Days(TextChoices):
        EVEN_DAY = 'event day', 'Event day'
        ODD_DAY = 'odd day', 'Odd day'
        MONDAY = 'monday', 'Monday'
        TUESDAY = 'tuesday', 'Tuesday'
        WEDNESDAY = 'wednesday', 'Wednesday'
        THURSDAY = 'thursday', 'Thursday'
        FRIDAY = 'friday', 'Friday'
        SATURDAY = 'saturday', 'Saturday'

    name = CharField(max_length=50)
    teacher = OneToOneField('users.User', SET_NULL, null=True, blank=True)
    day = CharField(max_length=20, choices=Days.choices)
    room = ForeignKey('group.Room', SET_NULL, null=True, blank=True)
    course_start_date = DateField()
    course_end_date = DateField()
    course_start_time = TimeField()
    course = ForeignKey('group.Course', SET_NULL, null=True, blank=True)


class SkippedClass(Model):
    student = ForeignKey('users.User', CASCADE)
    group = ForeignKey('group.Group', CASCADE)
    date = DateField()


class Debtor(Model):
    student = ForeignKey('users.User', CASCADE)
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
