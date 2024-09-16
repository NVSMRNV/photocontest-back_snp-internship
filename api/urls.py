from django.urls import path

from api.views.users.views import HomeView, LoginUserView, LogoutUserView, RegisterUserView


urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]