import streamlit as st


def settings_page():
    st.title("Settings")
    st.subheader("Customize your Handy Recipes experience")

    dark_mode = st.toggle("Dark Mode")

    


if __name__ == "__main__":
    settings_page()