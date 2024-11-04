import streamlit as st
import cv2 as cv
from components.navbar import display_navbar
from pages.home_page import home_page
from pages.recipes_page import recipes_page

class App:
    def __init__(self):
        self.cap = cv.VideoCapture(0)
        st.set_page_config(layout="wide", page_title="Handy Recipes", page_icon="🤙")
        self.selected_option = display_navbar()  # Display navbar and store selected option

    def home_page(self):
        home_page()

    def recipes_page(self):
        recipes_page()

    def settings_page(self):
        st.title("Settings")
        st.write("This is where you can adjust settings for the app.")

    def about_page(self):
        st.title("About")
        st.write("Information about the Handy Recipes app.")

    def display_content(self):
        # Display the selected page based on the navbar option
        if self.selected_option == "Home":
            self.home_page()
        elif self.selected_option == "Recipes":
            self.recipes_page()  # Call the real-time hand detection in "Recipes"
        elif self.selected_option == "Settings":
            self.settings_page()
        elif self.selected_option == "About":
            self.about_page()

if __name__ == "__main__":
    app = App()
    app.display_content()