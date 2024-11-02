from django.urls import path

from apps.views import GroupListAPIView, GroupCreateAPIView, GroupRetrieveUpdateDestroyAPIView, \
    SkippedClassListCreateAPIView, RoomListCreateAPIView, UserCreateAPIView, UserListAPIView, CourseCreateAPIView

urlpatterns = [
    path('group/list/', GroupListAPIView.as_view()),
    path('group/create/', GroupCreateAPIView.as_view()),
    path('group/update-delete-detail/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('skipeed-list-create/', SkippedClassListCreateAPIView.as_view()),
    path('room/list-create/', RoomListCreateAPIView.as_view()),
    path('user/create/', UserCreateAPIView.as_view()),
    path('user/list/', UserListAPIView.as_view()),
    path('user/detail-update-delete/', UserListAPIView.as_view()),
    path('course/create/', CourseCreateAPIView.as_view()),
]
