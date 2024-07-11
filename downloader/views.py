from django.shortcuts import render
from pytube import YouTube


def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        yt = YouTube(url)
        video = yt
        print(yt)
        return render(request, 'index.html', {"data": video})
    return render(request, 'index.html')

def download_list(request):
    return render(request, "index.html")