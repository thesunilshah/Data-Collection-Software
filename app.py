import streamlit as st
from streamlit_option_menu import option_menu

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
        st.write(f"Hello, you are in {selected}!")
    elif selected == "Image Processing":
        st.write(f"Hello, you are in {selected}!")
    elif selected == "Text Analysis":
        st.write(f"Hello, you are in {selected}!")
    elif selected == "Final Data":
        st.write(f"Hello, you are in {selected}!")

if __name__ == "__main__":
    main()
