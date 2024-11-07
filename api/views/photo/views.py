from tokenize import Token
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from models_app.models.photo.models import Photo
from api.serializers.photos.serializers import CreatePhotoSerializer, RetrievePhotoSerializer


class ListPhotoAPIView(APIView):
    def get(self, request: HttpRequest):
        photos = Photo.objects.all()
        serializer = RetrievePhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrievePhotoAPIView(APIView):
    def get(self, request: HttpRequest, pk):
        try:
            photo = Photo.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Объект не найден.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RetrievePhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeletePhotoAPIView(APIView):
    ...


class UpdatePhotoAPIView(APIView):
    ...


class CreatePhotoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request: HttpRequest):
        request.data['user'] = request.user.id
        serializer = CreatePhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'photo': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)