from django.db import models


from audio_converter.models import VoiceRecording


# Create your models here.
class Transcription(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    record = models.ForeignKey(VoiceRecording, related_name='transcriptions', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Транскрипция {self.id}"