from django.urls import path

from apps.views import GroupListAPIView, GroupCreateAPIView, GroupRetrieveUpdateDestroyAPIView, \
    SkippedClassListCreateAPIView, RoomListCreateAPIView, UserCreateAPIView, UserListAPIView

urlpatterns = [
    path('list/', GroupListAPIView.as_view()),
    path('create/', GroupCreateAPIView.as_view()),
    path('update-delete-detail/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('skipeed-list-create/', SkippedClassListCreateAPIView.as_view()),
    path('room-list-create/', RoomListCreateAPIView.as_view()),
    path('create/', UserCreateAPIView.as_view()),
    path('list/', UserListAPIView.as_view()),
    path('detail-update-delete/', UserListAPIView.as_view()),
]
