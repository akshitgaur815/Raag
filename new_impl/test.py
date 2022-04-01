import youtube_dl



def down_song(filename, url):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': filename,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    down_song('barkha.wav', 'https://www.youtube.com/watch?v=BAc2Pwyw_UM')