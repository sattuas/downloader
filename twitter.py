import yt_dlp


def twitter_downloader(url, output="video_twitter.%(ext)s"):
    options = {
        'outtmpl': output,
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = "https://x.com/RankRante/status/1951468499458728286"
    twitter_downloader(url)