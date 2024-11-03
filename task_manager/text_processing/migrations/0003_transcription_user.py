# Generated by Django 4.2.16 on 2024-11-03 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('text_processing', '0002_remove_transcription_call_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcription',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transcriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
