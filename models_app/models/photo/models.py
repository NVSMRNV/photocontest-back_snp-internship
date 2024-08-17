from django.db import models
from ..user.models import User


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=128)
    description = models.TextField()
    image_original = models.ImageField(upload_to='photos/original/')
    image_thumbnail = models.ImageField(upload_to='photos/thumbnails/')
    status = models.CharField(max_length=20, choices=[('pending', 'На модерации'), ('approved', 'Одобрена'), ('rejected', 'Отклонена')])
    likes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'photos'

    def __str__(self) -> str:
        return self.title
