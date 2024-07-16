import yt_dlp
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ydl_opts = {
  'format': 'bestaudio/best',
  'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
  }],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    for format in info.get('formats', []):
      print(f"{format['ext']}")