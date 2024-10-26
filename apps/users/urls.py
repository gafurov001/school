from django.urls import path

from users.views import UserCreateAPIView, UserListAPIView

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('list/', UserListAPIView.as_view()),
    path('detail-update-delete/', UserListAPIView.as_view()),
]
