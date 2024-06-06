import streamlit as st
from streamlit_option_menu import option_menu
import re
from error.errorhome import invalid_url_message

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
                    st.write(f"Playlist URL entered: {playlist_url}")
                else:
                    st.error(invalid_url_message())
            else:
                st.error("Please enter a YouTube playlist URL.")

    elif selected == "Image Processing":
        st.write(f"Hello, you are in {selected}!")
    elif selected == "Text Analysis":
        st.write(f"Hello, you are in {selected}!")
    elif selected == "Final Data":
        st.write(f"Hello, you are in {selected}!")

if __name__ == "__main__":
    main()
