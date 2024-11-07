from rest_framework.serializers import ModelSerializer

from models_app.models.photo.models import Photo


class CreatePhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['user', 'title', 'description', 'image_original', 'image_thumbnail']

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)    
    

class RetrievePhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'user', 'title', 'description', 'image_original', 'image_thumbnail', 'status', 'likes']
