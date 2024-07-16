import os

import yt_dlp
from django.shortcuts import redirect, render
from pydub import AudioSegment


def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        ydl_opts = {}
        data = []
        videos = []
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            for format in info.get('formats', []):
                if is_video(format):
                    format['filesize'] = get_std_size(format)
                    videos.append(format)
                data.append(format)
        return render(request, 'index.html', {"data": data, "videos": videos, "url": url})
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

    # Convert the file to MP3
    mp3_file = os.path.splitext(file_path)[0] + ".mp3"
    audio = AudioSegment.from_file(file_path, format=format)
    audio.export(mp3_file, format="mp3")
    
    return redirect("/")

def is_video(data):
    return (
        data['ext'] == "mp4" 
        and 'height' in data 
        and 'filesize' in data 
        and data['filesize'] is not None
    )

def get_std_size(data):
    size = data['filesize'] 
    mb = round((size / (1024 * 1024)), 2)
    if mb > 1000:
        return f"{round(mb / 1000, 2)} GB"
    return f"{mb} MB"
    
    
    