import logging
import os
import speech_recognition as sr
from django.http import JsonResponse
from django.shortcuts import render
from pydub import AudioSegment
from rest_framework.views import APIView



logger = logging.getLogger(__name__)


# Путь к файлу в корне проекта
ROOT_AUDIO_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp_audio.wav')


class Transcribe(APIView):
    def get( self, request, recording_id):
        try:
            # Проверяем, существует ли файл в корне проекта
            if not os.path.exists(ROOT_AUDIO_FILE_PATH):
                logger.error(f"Audio file {ROOT_AUDIO_FILE_PATH} does not exist")
                return JsonResponse({'error': 'Audio file does not exist'}, status=404)

            # Преобразуем аудиофайл в формат WAV
            wav_file_path = self.convert_audio_to_wav(ROOT_AUDIO_FILE_PATH)

            # Инициализация распознавателя
            recognizer = sr.Recognizer()

            # Открытие аудиофайла с помощью AudioFile
            with sr.AudioFile(wav_file_path) as source:
                # Настройка на шум окружающей среды
                recognizer.adjust_for_ambient_noise(source)
                # Запись аудио
                audio = recognizer.record(source)

            # Распознавание речи с использованием Google Web Speech API
            transcript = recognizer.recognize_google(audio, language='ru-RU')

            logger.info(f"Audio recording transcribed: {transcript}")

            # Удаляем временный файл WAV
            os.remove(wav_file_path)

            response = JsonResponse({'status': 'success', 'transcript': transcript},
                                    json_dumps_params={'ensure_ascii': False})
            response["Content-Type"] = "application/json; charset=utf-8"
            return response
        except sr.UnknownValueError:
            logger.error("Google Web Speech API could not understand audio")
            return JsonResponse({'error': 'Google Web Speech API could not understand audio'}, status=500)
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Web Speech API; {e}")
            return JsonResponse({'error': f'Could not request results from Google Web Speech API; {e}'}, status=500)
        except Exception as e:
            logger.error(f"Failed to transcribe audio file: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    def converter(self,  audio_file_path):
        try:
            # Проверяем, существует ли файл
            if not os.path.exists(audio_file_path):
                logger.error(f"Audio file {audio_file_path} does not exist")
                raise FileNotFoundError(f"Audio file {audio_file_path} does not exist")

            # Загружаем аудиофайл с помощью pydub
            audio = AudioSegment.from_file(audio_file_path)
            # Создаем временный файл для сохранения в формате WAV
            temp_wav_path = os.path.splitext(audio_file_path)[0] + "_temp.wav"
            # Экспортируем аудиофайл в формате WAV
            audio.export(temp_wav_path, format="wav")
            return temp_wav_path
        except Exception as e:
            logger.error(f"Failed to convert audio file {audio_file_path} to WAV: {e}")
            raise