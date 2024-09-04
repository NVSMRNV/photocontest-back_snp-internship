from django.db import models
from models_app.models.user.models import User
from models_app.models.base.models import BaseModel


class Photo(BaseModel):
    PEN = 'PENDING'
    APP = 'APPROVED'
    REJ = 'REJECTED'

    STATUS_CHOICES = (
        (PEN, 'На модерации'),
        (APP, 'Одобрена'),
        (REJ, 'Отклонена'),
    )
       
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=128)
    description = models.TextField()
    image_original = models.ImageField(upload_to='photos/original/')
    image_thumbnail = models.ImageField(upload_to='photos/thumbnails/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    likes = models.PositiveIntegerField(default=0)
   
    class Meta:
        db_table = 'photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self) -> str:
        return self.title

