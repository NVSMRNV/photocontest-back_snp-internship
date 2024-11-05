from django.urls import path

from api.views.users.views import LoginUserAPIView, RegisterUserAPIView, TestAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register' ),
    path('login/', LoginUserAPIView.as_view(), name='login'),
]