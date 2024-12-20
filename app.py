import streamlit as st

import cv2 as cv

from app_pages.home_page import home_page
from app_pages.about_page import about_page
from app_pages.recipes_page import recipes_page
from app_pages.how_to_use import how_to_use

from components.navbar import display_navbar

class App:
    def __init__(self):
        self.cap = cv.VideoCapture(0)
        st.set_page_config(layout="wide", page_title="Handy Recipes", page_icon="assets/HandyRecipes.png", initial_sidebar_state="collapsed")
        self.selected_option = display_navbar()  # Display navbar and store selected option
        hide_sidebar = """
            <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stSidebarNav"] {display: none;}
            #MainMenu { visibility: hidden; }
            footer { visibility: hidden; }
            </style>
        """
        st.markdown(hide_sidebar, unsafe_allow_html=True)


    def home_page(self):
        home_page()

    def recipes_page(self):
        recipes_page()

    def how_to_use_page(self):
        how_to_use()

    def about_page(self):
        about_page()

    def display_content(self):
        # Display the selected page based on the navbar option
        if self.selected_option == "Home":
            self.home_page()
        elif self.selected_option == "Recipes":
            self.recipes_page()  # Call the real-time hand detection in "Recipes"
        elif self.selected_option == "Tutorial":
            self.how_to_use_page()
        elif self.selected_option == "About":
            self.about_page()

if __name__ == "__main__":
    app = App()
    app.display_content()