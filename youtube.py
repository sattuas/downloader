from pytubefix import YouTube
from moviepy import AudioFileClip, VideoFileClip
import os
from utils import *


class YouTube:
    def __init__(self, url):
        self.url = YouTube(url)

    def download_audio(self):
        audios = []
        audios = self.url.streams.filter(only_audio=True, file_extension="webm")
        audios = sorted(audios, key=lambda s: int(s.abr.replace('kbps', '')), reverse=True)
        
        audio_m4a = audios[0]
        audio_m4a.download(filename="audio.m4a")

        mp3_converter = AudioFileClip("audio.m4a")
        mp3_converter.write_audiofile("audio_converted.mp3", logger=None)
        mp3_converter.close()

'''
def youtube_downloader(url):
    if url:
        yt = YouTube(url)

        audios = []
        audios = yt.streams.filter(only_audio=True, file_extension="webm")
        audios = sorted(audios, key=lambda s: int(s.abr.replace('kbps', '')), reverse=True)
        ys_mp3 = audios[0]
        ys_mp3.download(filename="audio.m4a")

        converter = AudioFileClip("audio.m4a")
        converter.write_audiofile("audio_converted.mp3", logger=None)
        converter.close()

        videos = []
        for video in yt.streams.filter(file_extension="mp4", only_video=True):
            if video.video_codec.startswith("avc1"):
                videos.append(video)

        count = 0
        for res in videos:
            print(f'[ {count} ] {res.resolution}')
            count += 1
        
        while True:
            select_res = int(input('select resolution: '))

            if select_res > len(videos) - 1 or select_res < 0:
                print('select a valid option')
            if select_res >= 0 and select_res <= len(videos) - 1:
                ys_mp4 = videos[select_res]
                ys_mp4.download(filename="video.mp4")
                break

        video = VideoFileClip("video.mp4")
        audio = AudioFileClip("audio_converted.mp3")

        audio = audio.with_duration(video.duration)
        video_with_audio = video.with_audio(audio)

        video_with_audio.write_videofile("download.mp4", codec="libx264", audio_codec="aac", logger=None)

        audiom4a_path = "audio.m4a"
        audio_temp = "audio_converted.mp3"
        video_temp = "video.mp4"
        
        if os.path.exists(audiom4a_path):
            os.remove(audiom4a_path)
            os.remove(audio_temp)
            os.remove(video_temp)
            print('arquivo m4a deletado!')
            return 'download realizado com sucesso! :)'
        else:
            print('arquivo não encontrado D:')
    else:
        return 'erro!'
    
'''