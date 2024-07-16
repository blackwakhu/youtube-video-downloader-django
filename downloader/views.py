import os

import yt_dlp
from django.shortcuts import redirect, render
# from pydub import AudioSegment
import subprocess

from .download_utilities import get_audio, get_video


def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        audio = get_audio(url)
        videos = get_video(url)
        return render(request, 'index.html', {"audio": audio, "videos": videos, "url": url})
    return render(request, 'index.html')

def download_list(request):
    return render(request, "index.html")

def download_video(request, format):
    url = request.GET.get('url')
    ydl_opts = {
        'outtmpl': os.path.expanduser("~/Downloads/%(title)s.%(ext)s"),
        'format': format
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return redirect("/")

def download_audio(request, format):
    url = request.GET.get('url')
    ydl_opts = {
        'outtmpl': os.path.expanduser("~/Downloads/%(title)s.%(ext)s"),
        'format': format
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    file_path = ydl.prepare_filename(ydl.extract_info(url, download=False))
    
    file_name = os.path.basename(file_path)
    last_dot_index = file_name.rfind(".")
    mp3_file = os.path.join(os.path.dirname(file_path), file_name[:last_dot_index] + ".mp3")
    
    subprocess.call(['ffmpeg', '-i', file_path, mp3_file])

    os.remove(file_path)
    
    return redirect("/")




    

    
    
    