from django.db import models

from app.models import MyUser


# Create your models here.
class Transcription(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    call_at = models.DateTimeField()
    user = models.ForeignKey(MyUser, related_name='transcriptions', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Транскрипция {self.id}"