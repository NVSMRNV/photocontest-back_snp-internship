from django.db import models
from models_app.models.user.models import User
from models_app.models.photo.models import Photo
from models_app.models.base.models import BaseModel 


class Vote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='votes')

    class Meta:
        db_table = 'votes'
        unique_together = ('user', 'photo')
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'

    def __str__(self) -> str:
        return f'{self.user.username} проголосовал за {self.photo.title}'
