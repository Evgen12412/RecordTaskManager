import os

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from audio_converter.models import VoiceRecording


class TaskStatusView(APIView):
    def post(self, request, user_id):
        task_status = request.data.get('task')
        task_id = request.data.get('task_id')
        # Здесь можно добавить логику для обработки статуса задачи
        if task_status == 'run':
            # Логика для обработки статуса 'run'
            try:
                recording = VoiceRecording.objects.get(id=task_id)
                audio_file_path = recording.audio_file.path
                if os.path.exists(audio_file_path):
                    with open(audio_file_path, 'rb') as audio_file:
                        response = HttpResponse(audio_file.read(), content_type='audio/wav')
                        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(audio_file_path)}"'
                        return response
                else:
                    return JsonResponse({'status': 'error', 'message': 'Audio file not found'}, status=404)
            except VoiceRecording.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Recording not found'}, status=404)
        elif task_status == 'stop':
            # Логика для обработки статуса 'stop'
            pass
        elif task_status == 'send':
            # Логика для обработки статуса 'send'
            pass
        return JsonResponse({'status': 'success', 'task_status': task_status, 'task_id': task_id})




