from django.urls import path

from group.views import GroupListAPIView, GroupRetrieveUpdateDestroyAPIView, SkippedClassListCreateAPIView, \
    GroupCreateAPIView, RoomListCreateAPIView

urlpatterns = [
    path('list/', GroupListAPIView.as_view()),
    path('create/', GroupCreateAPIView.as_view()),
    path('update-delete-detail/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('skipeed-list-create/', SkippedClassListCreateAPIView.as_view()),
    path('room-list-create/', RoomListCreateAPIView.as_view()),
]
