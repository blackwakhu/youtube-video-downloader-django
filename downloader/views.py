import yt_dlp
from django.shortcuts import render


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
                    videos.append(format)
                data.append(format)
        return render(request, 'index.html', {"data": data, "videos": videos})
    return render(request, 'index.html')

def download_list(request):
    return render(request, "index.html")

def is_video(data):
    return data['ext'] == "mp4" and 'height' in data.keys() and 'filesize' in data.keys() and data['filesize'] is not None
# def get_video(data):
    
    