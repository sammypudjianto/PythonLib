import youtube_dl as dl

ydl_opts = {
    'format': 'best',  # best[height=720]
    'outtmpl': f'%(title)s.%(ext)s',
    'nooverwrites': True,
    'no_warnings': False,
    'ignoreerrors': True
}
with dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(
        [

        ]
    )
