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
                if format['ext'] == "mp4":
                    if 'height' in format.keys():
                        videos.append(format)
                data.append(format)
        return render(request, 'index.html', {"data": data, "videos": videos})
    return render(request, 'index.html')

def download_list(request):
    return render(request, "index.html")