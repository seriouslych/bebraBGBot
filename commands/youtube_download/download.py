import glob
import os

from yt_dlp import YoutubeDL

def video_download(base_dir, url, log):
    temp_dir = os.path.join(base_dir, 'temp')
    save_path = os.path.join(temp_dir, '%(title)s.%(ext)s')
    glob_path = os.path.join(temp_dir, '*')

    save_options = {
        'outtmpl': save_path,
    }
    try:
        with YoutubeDL(save_options) as ydl:
            ydl.download([url])
            # Возвращаем имя последнего скачанного файла
            downloaded_files = glob.glob(glob_path)
            if downloaded_files:
                return downloaded_files[-1]
            else:
                raise ValueError("Не удалось найти скачанный файл")
    except Exception as e:
        log.exception(f"Ошибка скачивания: {e}")
        return None

def audio_download(base_dir, url, log):
    temp_dir = os.path.join(base_dir, 'temp')
    save_path = os.path.join(temp_dir, '%(title)s.%(ext)s')
    ffmpeg_path = os.path.join(base_dir, 'ffmpeg')
    glob_path = os.path.join(temp_dir, '*')

    
    save_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '328',
        }],
        'outtmpl': save_path,
        'ffmpeg_location': ffmpeg_path
    }

    with YoutubeDL(save_options) as ydl:
        try:
            ydl.download([url])
            
            downloaded_files = glob.glob(glob_path)
            if downloaded_files:
                return downloaded_files[-1]
            else:
                raise ValueError("Не удалось найти скачанный файл")
        except Exception as e:
            log.exception(f"Ошибка скачивания: {e}")
            return None
