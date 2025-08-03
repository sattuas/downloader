from utils import *
from youtube import *
from twitter import *


while True:

    print(f'[ 1 ] {set_color('YOUTUBE', 'red')}')
    print(f'[ 2 ] {set_color('X/TWITTER', "#1900FF")}')

    try:
        option = int(input('select an option: '))
    except Exception as e:
        print(f'error! {e}')
    finally:
        if option == 1:
            link = str(input('paste a youtube link here: '))
            youtube_downloader(link)
        if option == 2:
            link = str(input('paste a x/twitter link here: '))
            twitter_downloader(link)

    