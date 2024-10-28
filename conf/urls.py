from django.contrib import admin
from django.urls import include, path, re_path

from api.views.users.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
]
