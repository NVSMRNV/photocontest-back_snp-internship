from django.urls import path

from api.views.photo.views import CreatePhotoAPIView, ListPhotoAPIView, RetrievePhotoAPIView
from api.views.users.views import LoginUserAPIView, RegisterUserAPIView

urlpatterns = [
    path('photos/', ListPhotoAPIView.as_view(), name='list-photos'),
    path('create/', CreatePhotoAPIView.as_view(), name='create-photo'),
    path('retrieve/<int:pk>/', RetrievePhotoAPIView.as_view(), name='retrieve-photo'),
    path('register/', RegisterUserAPIView.as_view(), name='register' ),
    path('login/', LoginUserAPIView.as_view(), name='login'),
]