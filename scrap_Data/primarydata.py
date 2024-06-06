import os
import json
import requests
from pytube import Playlist
from PIL import Image
from io import BytesIO

class PrimaryData:
    def __init__(self, url):
        self.url = url
        self.data_folder = 'data'
        self.image_folder = os.path.join(self.data_folder, 'images')
        self.create_data_folder()

    def create_data_folder(self):
        # Create the data and images directories if they don't exist
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)

    def print_playlist_videos(self):
        # Print the URL
        print(f"URL provided: {self.url}")
        
        # Using pytube to get and print all video URLs in the playlist
        try:
            playlist = Playlist(self.url)
            for video_url in playlist.video_urls:
                print(video_url)
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def text_data(self):
        try:
            playlist = Playlist(self.url)
            videos_data = []
            
            for video in playlist.videos:
                video_id = video.video_id
                thumbnail_path = self.thumbnail_downloader(video.thumbnail_url, video_id)
                if thumbnail_path:
                    video_info = {
                        'title': video.title,
                        'views': video.views,
                        'thumbnail_url': thumbnail_path
                    }
                    videos_data.append(video_info)
            
            # Save data to a JSON file
            json_file_path = os.path.join(self.data_folder, 'playlist_data.json')
            with open(json_file_path, 'w') as json_file:
                json.dump(videos_data, json_file, indent=4)
            
            print(f"Data saved to {json_file_path}")
        
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def thumbnail_downloader(self, url, video_id):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                if image.format in ["JPEG", "JPG", "PNG"]:
                    image_path = os.path.join(self.image_folder, f"{video_id}.{image.format.lower()}")
                    image.save(image_path)
                    print(f"Downloaded thumbnail for video {video_id}")
                    return image_path  # Return the local path to the downloaded thumbnail
                else:
                    print(f"Invalid image format for video {video_id}: {image.format}")
                    return None
            else:
                print(f"Failed to download thumbnail for video {video_id}: Status code {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while downloading thumbnail for video {video_id}: {e}")
            return None

# Example usage
# if __name__ == "__main__":
#     url = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
#     primary_data = PrimaryData(url)
#     primary_data.print_playlist_videos()
#     primary_data.text_data()
