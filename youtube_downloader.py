from pytube import YouTube
import os

def download_video(url, save_path='videos/'):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(save_path)
    return f"{save_path}{yt.title}.mp4"