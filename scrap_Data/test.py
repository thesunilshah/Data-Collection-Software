import os
import json
import requests
from pytube import Playlist
from bs4 import BeautifulSoup
from PIL import Image

class PrimaryData:
    def __init__(self, playlist_url):
        self.playlist_url = playlist_url
        self.data_folder = 'data'
        self.images_folder = os.path.join(self.data_folder, 'images')
        os.makedirs(self.data_folder, exist_ok=True)
        os.makedirs(self.images_folder, exist_ok=True)
        self.json_file_path = os.path.join(self.data_folder, 'playlist_data.json')
        self.playlist_data = []

    def text_data(self):
        playlist = Playlist(self.playlist_url)
        for video in playlist.videos:
            video_id = video.video_id
            video_data = {
                'title': video.title,
                'tags': video.keywords,
                'views': video.views,
                'url': video.watch_url,
                'category': self.category(video.watch_url)  # Get category
            }
            self.download_thumbnail(video.thumbnail_url, video_id)
            video_data['thumbnail_path'] = os.path.join('data', 'images', f'{video_id}.jpg')
            self.playlist_data.append(video_data)
        
        # Save data to JSON
        with open(self.json_file_path, 'w') as json_file:
            json.dump(self.playlist_data, json_file, indent=4)

    def download_thumbnail(self, video_id):
        try:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                thumbnail_path = os.path.join(self.images_folder, f'{video_id}.jpg')
                with open(thumbnail_path, 'wb') as img_file:
                    img_file.write(response.content)
                # Check if the image is valid
                self.check_image(thumbnail_path)
            else:
                print(f"Failed to download thumbnail for {video_id}.")
        except Exception as e:
            print("An error occurred while downloading the thumbnail:", str(e))

    def check_image(self, image_path):
        try:
            img = Image.open(image_path)
            img.verify()
        except (IOError, SyntaxError) as e:
            print(f"Image at {image_path} is corrupted. Removing it.")
            os.remove(image_path)

    def category(self, video_url):
        try:
            response = requests.get(video_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                category_element = soup.find('meta', attrs={'itemprop': 'genre'})
                if category_element:
                    category = category_element.get('content')
                    return category
            return "Unknown"
        except Exception as e:
            print("An error occurred:", str(e))
            return "Unknown"
