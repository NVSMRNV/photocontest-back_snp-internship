from django.urls import include, path

from api.views.users.views import LoginUserAPIView, RegisterUserAPIView
from api.views.photo.views import CreatePhotoAPIView, ListPhotoAPIView, RetrievePhotoAPIView

from api.docs.basics.schema import schema_view


users_api_urlpatterns = [
   path('login/', LoginUserAPIView.as_view(), name='users-login'),
   path('registration/', RegisterUserAPIView.as_view(), name='users-registration' ),
]

photos_api_urlpatterns = [
   path('list/', ListPhotoAPIView.as_view(), name='photos-list'),
   path('creation/', CreatePhotoAPIView.as_view(), name='photos-creation'),
   path('retrieval/<int:pk>/', RetrievePhotoAPIView.as_view(), name='photos-retrieval'),
]

docs_api_urlpatterns = [
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = [
   path('v1/users/', include(users_api_urlpatterns)),
   path('v1/photos/', include(photos_api_urlpatterns)),
   path('v1/docs/', include(docs_api_urlpatterns)),
]
