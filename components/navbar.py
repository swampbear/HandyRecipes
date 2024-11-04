# navbar.py
from streamlit_option_menu import option_menu

def display_navbar():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Recipes", "Settings", "About"],  # Added "Recipes"
        icons=["house", "book", "gear", "info-circle"],  # Added an icon for "Recipes"
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    return selected