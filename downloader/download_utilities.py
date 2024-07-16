import yt_dlp


def get_video(url):
    ydl_opts = {}
    videos = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        for format in info.get('formats', []):
            if is_video(format):
                format['filesize'] = get_std_size(format)
                videos.append(format)
    return videos
    
def get_audio(url):
  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
  }
  audio = []
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(url, download=False)
      for format in info.get('formats', []):
          if is_audio(format):
              format['filesize'] = get_std_size(format)
              audio.append(format)
  return audio

def is_video(data):
    return (
        data['ext'] == "mp4" 
        and 'height' in data 
        and 'filesize' in data 
        and data['filesize'] is not None
    )

def is_audio(data):
    return (
        data['ext'] == "m4a" 
        and 'filesize' in data 
        and data['filesize'] is not None
    )

def get_std_size(data):
    size = data['filesize'] 
    mb = round((size / (1024 * 1024)), 2)
    if mb > 1000:
        return f"{round(mb / 1000, 2)} GB"
    return f"{mb} MB"
