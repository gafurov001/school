from django.urls import path

from apps.views import GroupListAPIView, GroupCreateAPIView, \
    StudentCreateAPIView, StudentListAPIView, CourseCreateAPIView, \
    StudentDestroyAPIView, StudentUpdateAPIView, StudentRetrieveAPIView, GroupUpdateAPIView, GroupDestroyAPIView, \
    GroupRetrieveAPIView, RoomCreateAPIView, RoomListAPIView, SkippedClassCreateAPIView, SkippedClassListAPIView, \
    WorkerCreateAPIView, WorkerListAPIView, WorkerDestroyAPIView, WorkerUpdateAPIView, WorkerRetrieveAPIView

urlpatterns = [
    path('group/list/', GroupListAPIView.as_view()),
    path('group/create/', GroupCreateAPIView.as_view()),
    path('group/update/<int:pk>/', GroupUpdateAPIView.as_view()),
    path('group/delete/<int:pk>/', GroupDestroyAPIView.as_view()),
    path('group/detail/<int:pk>/', GroupRetrieveAPIView.as_view()),
    path('skipeed/list/', SkippedClassListAPIView.as_view()),
    path('skipeed/create/', SkippedClassCreateAPIView.as_view()),
    path('room/create/', RoomCreateAPIView.as_view()),
    path('room/list/', RoomListAPIView.as_view()),
    path('student/create/', StudentCreateAPIView.as_view()),
    path('student/list/', StudentListAPIView.as_view()),
    path('student/delete/<int:pk>', StudentDestroyAPIView.as_view()),
    path('student/update/<int:pk>', StudentUpdateAPIView.as_view()),
    path('student/detail/<int:pk>', StudentRetrieveAPIView.as_view()),
    path('worker/create/', WorkerCreateAPIView.as_view()),
    path('worker/list/', WorkerListAPIView.as_view()),
    path('worker/delete/<int:pk>', WorkerDestroyAPIView.as_view()),
    path('worker/update/<int:pk>', WorkerUpdateAPIView.as_view()),
    path('worker/detail/<int:pk>', WorkerRetrieveAPIView.as_view()),
    path('course/create/', CourseCreateAPIView.as_view()),
]
