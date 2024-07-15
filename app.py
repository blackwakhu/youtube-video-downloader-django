import yt_dlp

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

    print("Available formats:")
    for format in info.get('formats', []):
        print(f"  - {format['format_id']} - {format['ext']}")