import streamlit as st
from streamlit_option_menu import option_menu
import re
import os
import json
import pandas as pd
from PIL import Image
from errorhandling.errorHome import invalid_url_message
from scrap_Data.primarydata import PrimaryData

def main():
    st.title("YouTube Data Extraction Project")

    # Create a sidebar with navigation options
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # required
            options=["Home", "Image Processing", "Text Analysis", "Final Data"],  # required
            icons=["house", "image", "file-text", "database"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )

    # Display the selected page
    if selected == "Home":
        st.header("Welcome to Data Collection Software")
        st.subheader("Please paste a YouTube playlist URL to extract the data (Note: playlist must be public)")

        # Input box for the YouTube playlist URL
        playlist_url = st.text_input("YouTube Playlist URL")

        # Submit button
        if st.button("Submit"):
            # Validate the URL
            if playlist_url:
                # Regular expression to check if the URL is a YouTube playlist URL
                pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.*(list=)"
                if re.match(pattern, playlist_url):
                    # Handle the URL and extract text data
                    primary_data = PrimaryData(playlist_url)
                    primary_data.text_data()
                    st.write(f"Playlist URL entered: {playlist_url}")
                    st.success("Data extracted and saved successfully.")
                else:
                    st.error(invalid_url_message())
            else:
                st.error("Please enter a YouTube playlist URL.")

        # Display 6 sample images from the data/images folder in a tabular form
        st.subheader("Sample Thumbnails")
        image_folder = os.path.join('data', 'images')
        if os.path.exists(image_folder):
            image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png'))]
            if image_files:
                sample_images = image_files[:6]
                cols = st.columns(3)  # Creating 3 columns for the images
                for idx, img_path in enumerate(sample_images):
                    img = Image.open(img_path)
                    cols[idx % 3].image(img, caption=os.path.basename(img_path), use_column_width=True)
            else:
                st.write("No images found in the images folder.")
        else:
            st.write("Images folder does not exist.")

        # Display 10 sample JSON data entries from the data/playlist_data.json file using pandas
        st.subheader("Sample JSON Data")
        json_file_path = os.path.join('data', 'playlist_data.json')
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                playlist_data = json.load(json_file)
                sample_data = playlist_data[:10]
                df = pd.DataFrame(sample_data)
                st.dataframe(df)
        else:
            st.write("JSON file does not exist.")

    elif selected == "Image Processing":
        st.write(f"Hello, you are in {selected}!")
    elif selected == "Text Analysis":
        st.write(f"Hello, you are in {selected}!")
    elif selected == "Final Data":
        st.write(f"Hello, you are in {selected}!")

if __name__ == "__main__":
    main()
