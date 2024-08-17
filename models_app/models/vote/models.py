from django.db import models
from ..user.models import User
from ..photo.models import Photo


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='votes')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'votes'
        unique_together = ('user', 'photo')

    def __str__(self) -> str:
        return f'{self.user.username} проголосовал за {self.photo.title}'
    