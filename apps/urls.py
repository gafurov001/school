from django.urls import path

from apps.views import GroupListAPIView, GroupCreateAPIView, \
    SkippedClassListCreateAPIView, RoomListCreateAPIView, UserCreateAPIView, UserListAPIView, CourseCreateAPIView, \
    UserDestroyAPIView, UserUpdateAPIView, UserRetrieveAPIView, GroupUpdateAPIView, GroupDestroyAPIView, \
    GroupRetrieveAPIView

urlpatterns = [
    path('group/list/', GroupListAPIView.as_view()),
    path('group/create/', GroupCreateAPIView.as_view()),
    path('group/update/<int:pk>/', GroupUpdateAPIView.as_view()),
    path('group/delete/<int:pk>/', GroupDestroyAPIView.as_view()),
    path('group/detail/<int:pk>/', GroupRetrieveAPIView.as_view()),
    path('skipeed-list-create/', SkippedClassListCreateAPIView.as_view()),
    path('room/list-create/', RoomListCreateAPIView.as_view()),
    path('user/create/', UserCreateAPIView.as_view()),
    path('user/list/', UserListAPIView.as_view()),
    path('user/delete/<int:pk>', UserDestroyAPIView.as_view()),
    path('user/update/<int:pk>', UserUpdateAPIView.as_view()),
    path('user/detail/<int:pk>', UserRetrieveAPIView.as_view()),
    path('course/create/', CourseCreateAPIView.as_view()),
]
