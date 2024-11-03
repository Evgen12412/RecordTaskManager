# Generated by Django 4.2.16 on 2024-11-03 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio_converter', '0001_initial'),
        ('text_processing', '0003_transcription_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcription',
            name='record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transcriptions', to='audio_converter.voicerecording'),
        ),
    ]