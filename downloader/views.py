from django.shortcuts import render
import yt_dlp


def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        ydl_opts = {}
        data = []
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            for format in info.get('formats', []):
                data.append(format)
        return render(request, 'index.html', {"data": data})
    return render(request, 'index.html')

def download_list(request):
    return render(request, "index.html")