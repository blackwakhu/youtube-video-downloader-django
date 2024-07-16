import yt_dlp

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

    print("Available formats:")
    for format in info.get('formats', []):
        if format['ext'] == "mp4":
            # if 'format_note' not in format.keys():
            #     format['format_note'] = "video"
            # print(f"{format['format_note']}")
            # if 'height' not in format.keys():
            #     format['height'] = "None"
            # if  'filesize' not in format.keys():
            #     format['filesize'] = 'None'
            # print(f"  - {format['format_id']} - {format['ext']} {format['height']}p {format['filesize']} {format['format']}")
            print(f"{format.keys()}")
            
        # else:
            # print(f"  - {format['format_id']} - {format['ext']}")
            
        # print(f"{format.keys()}")