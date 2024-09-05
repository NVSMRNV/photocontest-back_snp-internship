from rest_framework import generics
from models_app.models.user.models import User
from serializers.user.serializers import UserSerializer


#! Used for create-only endpoints.
#! Provides a post method handler.
class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    

#! Used for read-only endpoints to represent a collection of model instances.
#! Provides a get method handler.
class ListUserAPIView(generics.ListAPIView):
    serializer_class = UserSerializer


#! Used for read-only endpoints to represent a single model instance.
#! Provides a get method handler.
class RetrieveUserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer


#! Used for delete-only endpoints for a single model instance.
#! Provides a delete method handler.
class DestroyUserAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer


#! Used for update-only endpoints for a single model instance.
#! Provides put and patch method handlers.
class UpdateUserAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer