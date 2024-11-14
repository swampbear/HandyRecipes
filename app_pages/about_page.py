import streamlit as st
import base64
from pathlib import Path

linkedin_jobjorn = "https://www.linkedin.com/in/jobjorn-myren-246425266/"
linkedin_siri = "https://www.linkedin.com/in/siri-norstrand-eielsen-43608724a/"
linkedin_sondre = "https://www.linkedin.com/in/ness-development/"

team_members = [
    {"name": "Jobjørn Myren", "image": "assets/jobjorn.jpeg", "linkedin": linkedin_jobjorn, "bio": "Backend Developer, data handling specialist."},
    {"name": "Sondre Langedal Ness", "image": "assets/sondre.jpeg", "linkedin": linkedin_sondre, "bio": "Frontend Developer, gesture interaction expert."},
    {"name": "Siri Norstrand Eielsen", "image": "assets/siri.jpeg", "linkedin": linkedin_siri, "bio": "UI/UX Designer, ensures a user-friendly experience."},
]

def about_page():
    generateIntroHTML(),
    generateCards(),
    generateTeamMemberHTML()


def generateCards():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div></div>", unsafe_allow_html=True)
    with col2:
        generateKeyFeaturesHTML()
    with col3:
        generateTechStackHTML()
    with col4:
        st.markdown("<div></div>", unsafe_allow_html=True)


def generateIntroHTML():
    info_html = """\
    <div style="
        padding: 5px 10px; 
        text-align: center; 
        max-width: 50%; 
        margin: 0 auto 20px auto;
        border-radius: 22px;
        background-color: {};
        ">
        <h1>What is HandyRecipes?</h1>
        <p style="font-size: 18px;">HandyRecipes is an innovative web app designed to make cooking easier and cleaner! The app not only provides you with a variety of tasty recipes but also features a unique gesture-based step traversal system. By simply showing your index finger to the camera, you can move through different recipe steps without ever touching your device. This means no more greasy screens or messy pages – just effortless cooking!</p>
        <p style="font-size: 18px;">We hope HandyRecipes becomes a trusted companion in your kitchen, making cooking not only easier but also a lot more fun!</p>
    </div>
    """.format(st.get_option("theme.secondaryBackgroundColor"))

    st.markdown(info_html, unsafe_allow_html=True)

def generateKeyFeaturesHTML():
    feature_html = """\
        <div style="
            background-color: {}; 
            border-radius: 22px; 
            padding: 40px 20px;
            min-height: 620px;
        ">
    """.format(
        st.get_option("theme.primaryColor")
        )

    feature_html += """\
        <h2 style="text-align: center; margin-bottom: 20px;">Key Features</h2>            
    """

    feature_html += """\
    <ol>
    {}{}{}{}{}{}
    </ol>
    """.format(
        row("Gesture-Based Navigation", "Move through recipe steps by showing your index finger to the camera. Perfect for when your hands are messy."),
        row("Recipe Database", "A well-structured JSON format makes it easy to add, update, or remove recipes."),
        row("Recipe Components", "Each recipe breaks down ingredients into components (e.g., 'Sauce,' 'Base') with specified portion sizes."),
        row("Step-by-Step Instructions", "Detailed guidance for each recipe ensures easy and accurate cooking."),
        row("Streamlit Interface", "User-friendly browsing and recipe selection experience with clear display of components, ingredients, and steps."),
        row("Dynamic Recipe Handling", "JSON parsing and a custom service layer allow for efficient and dynamic handling of recipe data.")
        )

    st.markdown(feature_html, unsafe_allow_html=True)

def generateTechStackHTML():
    tech_html = """\
         <div style="
            background-color: {}; 
            border-radius: 22px; 
            padding: 40px 20px;
            min-height: 620px;
        ">
    """.format(st.get_option("theme.primaryColor"))

    tech_html += """\
        <h2 style="text-align: center; margin-bottom: 20px;">Technologies Used</h2>            
    """

    tech_html += """\
    <ol>
    {}{}{}
    </ol>
    """.format(
        row("OpenCV", "Computer vision library for accessing the device's camera."),
        row("MediaPipe", "Integrated with OpenCV for gesture recognition."),
        row("Hand Estimation Class", "Adapted from <a href='https://gautamaditee.medium.com/hand-recognition-using-opencv-a7b109941c88' no-referrer target=_blank>Hand Detection Tracking in Python using OpenCV and MediaPipe</a>, this class is responsible for drawing nodes, edges, and registering finger gestures.")
    )

    st.markdown(tech_html, unsafe_allow_html=True)

def generateTeamMemberHTML():
    col1, col2, col3 = st.columns(3)

    team_html = """\
        <div style="
            background-color: {}; 
            border-radius: 22px; 
            padding: 40px 20px;
            max-width: 50%;
            margin: 0 auto 20px auto;
        ">
    """.format(st.get_option("theme.secondaryBackgroundColor"))

    team_html += """\
        <h2 style="text-align: center; margin-bottom: 20px;">Meet the Team</h2>
        <div style="
            display: flex;
            flex-direction: row;
            justify-content: space-around;
        ">
        """

    for i, col in enumerate([col1, col2, col3]):
        member = team_members[i]
        with col:
            team_html += """\
                <div style="text-align: center; line-height: 5px">
                    {}
                    <h3>{}</h3>
                    <p>{}</p>
                    <a href="{}" target="_blank" style="text-decoration: none; color: #0077b5;">
                        LinkedIn Profile
                    </a>
                </div>
                """.format(img_to_html(member['image']), member['name'], member['bio'], member['linkedin'])
    
    team_html += """\
        </div>
        </div>
        """
    
    st.markdown(team_html, unsafe_allow_html=True)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' style='width: 250px; height: 250px; border-radius: 50%; margin-bottom: 10px'>".format(
      img_to_bytes(img_path)
    )
    return img_html

def row(label, value):
    return f"""
    <li>
        <div style="font-weight: bold; font-size: 16px;">{label}:</div>
        <em> - {value}</em>
    </li>
    """


if __name__ == "__main__":
    about_page()
