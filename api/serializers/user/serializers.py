from rest_framework import serializers
from models_app.models.user.models import User


class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = ('id', 'email', 'username',)
        