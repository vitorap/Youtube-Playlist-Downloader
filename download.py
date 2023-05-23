from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
import eyed3
import os
import requests
from bs4 import BeautifulSoup

def get_playlist_title(playlist_url):
    page = requests.get(playlist_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.title.string.partition('-')[0].strip()

def download_audio(url, download_folder):
    try:
        yt = YouTube(url)
        download_stream = yt.streams.filter(only_audio=True).first()
        download_file = download_stream.download(download_folder)
        mp3_file = os.path.splitext(download_file)[0] + '.mp3'
        
        # Convert mp4 audio to mp3
        audio_clip = AudioFileClip(download_file)
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        
        # Delete the original mp4 audio file
        os.remove(download_file)
        
        # Add ID3 tag to mp3 file
        audio_file = eyed3.load(mp3_file)
        if(audio_file.tag is None):
            audio_file.initTag()

        audio_file.tag.title = yt.title
        audio_file.tag.save()

        print(f'Successfully downloaded {yt.title} as mp3')
    except Exception as e:
        print(f'Error downloading {url}: {e}')

def download_playlist(playlist_url, download_path):
    try:
        playlist = Playlist(playlist_url)
        
        # Get playlist title and create a specific folder for the playlist
        playlist_title = get_playlist_title(playlist_url)
        download_folder = os.path.join(download_path, playlist_title)
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        for url in playlist.video_urls:
            download_audio(url, download_folder)
    except Exception as e:
        print(f'Error downloading playlist: {e}')

def main():
    playlist_url = input('Enter the URL of the YouTube playlist: ')
    download_path = input('Enter the download path: ')
    
    # Create download directory if not exist.
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    download_playlist(playlist_url, download_path)

if __name__ == '__main__':
    main()
