import streamlit as st

def home_page():
    st.title("Handy Recipes")
    st.subheader("Navigate through food recipes using hand gestures")
    st.text("No need to make your keyboard or touchscreen dirty!")

    st.markdown("""
    ## Features:
    - Browse recipes with hand gestures
    - Save your favorite recipes
    - Share recipes with friends
    - Get personalized recipe recommendations

    ## How to Use:
    1. Enable your webcam
    2. Use hand gestures to navigate through the recipes
    3. Enjoy cooking without touching your device!

    ## Popular Recipes:
    - Spaghetti Carbonara
    - Chicken Alfredo
    - Vegan Tacos
    - Chocolate Cake

    ## Get Started:
    Click the button below to start exploring recipes with hand gestures!
    """)

if __name__ == "__main__":
    home_page()