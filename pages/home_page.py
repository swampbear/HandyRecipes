import streamlit as st

def home_page():
    st.title("Handy Recipes")
    st.subheader("Navigate through food recipes using hand gestures")
    st.markdown(""" 
        *Browse recipes, save favorites, share with friends,
        and get personlized recommandations - all with* **simple hand gestures**!
    """)
    st.text("No need to make your keyboard or touchscreen dirty!")

    getstarted = ("""
        ## Get Started:
        1. Enable your webcam
        2. Use hand gestures to navigate through the recipes
        3. Enjoy cooking without touching your device!
                                    
        **Click the button below to start exploring recipes with hand gestures!**
    """)

    features = ("""
        ## Features:
        - Browse recipes with hand gestures
        - Save your favorite recipes
        - Share recipes with friends
        - Get personalized recipe recommendations
    """)
        
    howtouse = ("""
        ## How to Use:
        1. Enable your webcam
        2. Use hand gestures to navigate through the recipes
        3. Enjoy cooking without touching your device!
    """)
        
    popular = (""" 
        ### Popular Recipes:
        - Spaghetti Carbonara
        - Chicken Alfredo
        - Vegan Tacos
        - Chocolate Cake
    """)

    with st.container(): 
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(getstarted)

        with col2:
            st.markdown(popular)
  
if __name__ == "__main__":
    home_page()