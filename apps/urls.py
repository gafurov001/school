from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.views import GroupListAPIView, GroupCreateAPIView, \
    StudentCreateAPIView, StudentListAPIView, CourseCreateAPIView, \
    StudentDestroyAPIView, StudentGenericAPIView, StudentRetrieveAPIView, GroupGenericAPIView, GroupDestroyAPIView, \
    GroupRetrieveAPIView, RoomCreateAPIView, RoomListAPIView, SkippedClassCreateAPIView, SkippedClassListAPIView, \
    WorkerCreateAPIView, WorkerListAPIView, WorkerDestroyAPIView, WorkerGenericAPIView, WorkerRetrieveAPIView, \
    RoomDestroyAPIView, RoomGenericAPIView, RoomRetrieveAPIView, StudentCountGenericAPIView, GroupCountGenericAPIView, \
    RoomCountGenericAPIView, WorkerCountGenericAPIView

urlpatterns = [
    path('group/list/', GroupListAPIView.as_view()),
    path('group/create/', GroupCreateAPIView.as_view()),
    path('group/update/<int:pk>/', GroupGenericAPIView.as_view()),
    path('group/delete/<int:pk>/', GroupDestroyAPIView.as_view()),
    path('group/detail/<int:pk>/', GroupRetrieveAPIView.as_view()),
    path('group/count/', GroupCountGenericAPIView.as_view()),
    path('skipeed/list/', SkippedClassListAPIView.as_view()),
    path('skipeed/create/', SkippedClassCreateAPIView.as_view()),
    path('room/create/', RoomCreateAPIView.as_view()),
    path('room/update/<int:pk>', RoomGenericAPIView.as_view()),
    path('room/delete/<int:pk>/', RoomDestroyAPIView.as_view()),
    path('room/detail/<int:pk>/', RoomRetrieveAPIView.as_view()),
    path('room/list/', RoomListAPIView.as_view()),
    path('room/count/', RoomCountGenericAPIView.as_view()),
    path('student/create/', StudentCreateAPIView.as_view()),
    path('student/list/', StudentListAPIView.as_view()),
    path('student/delete/<int:pk>', StudentDestroyAPIView.as_view()),
    path('student/update/<int:pk>', StudentGenericAPIView.as_view()),
    path('student/detail/<int:pk>', StudentRetrieveAPIView.as_view()),
    path('student/count', StudentCountGenericAPIView.as_view()),
    path('worker/create/', WorkerCreateAPIView.as_view()),
    path('worker/list/', WorkerListAPIView.as_view()),
    path('worker/delete/<int:pk>', WorkerDestroyAPIView.as_view()),
    path('worker/update/<int:pk>', WorkerGenericAPIView.as_view()),
    path('worker/detail/<int:pk>', WorkerRetrieveAPIView.as_view()),
    path('worker/count/', WorkerCountGenericAPIView.as_view()),
    path('course/create/', CourseCreateAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
