import streamlit as st

def home_page():
    with st.container():
        fuck, col1, col2, you = st.columns([1, 2, 2, 1])

        with fuck:
            st.markdown("<div></div>", unsafe_allow_html=True)

        with col1:
            html = """\
                <div style="
                    padding: 5px 10px; 
                    text-align: center; 
                    margin: 0 auto 20px auto;
                    border-radius: 22px;
                    background-color: {};
                    ">
                    <h1>Handy Recipes</h1>
                    <h2>Navigate through food recipes using hand gestures</h2>
                    <p>Browse recipes, save favorites, share with friends,
                    and get personlized recommandations - all with simple hand gestures!</p>
                    <p>No need to make your keyboard or touchscreen dirty!</p>
                </div>
            """.format(st.get_option("theme.secondaryBackgroundColor"))

            st.markdown(html, unsafe_allow_html=True)

            getstarted = """\
            <div style="
                    padding: 5px 10px;
                    border-radius: 22px;
                    background-color: {};
                    ">
                <h3 style="text-align: center">Get Started:</h3>
                <ol>
                <li>Enable your webcam</li>
                <li>Use hand gestures to navigate through the recipes</li>
                <li>Enjoy cooking without touching your device!</li>
                </ol>
            </div>
            """.format(st.get_option("theme.primaryColor"))
        
        with col2: 
            st.image("assets/Handtrace.png", width=250)

        with you:
            st.markdown("<div></div>", unsafe_allow_html=True)
        
        popular = """\
            <div style="
                    padding: 5px 10px;
                    border-radius: 22px;
                    background-color: {};
                    ">
                <h3 style="text-align: center">Popular Recipes:</h3>
                <ul>
                <li>Spaghetti Carbonara</li>
                <li>Vegan Tacos</li>
                <li>Chocolate Cake</li>
                </ul>
            </div>
            """.format(st.get_option("theme.primaryColor"))

    with st.container(): 
        fuck, col1, col2, you = st.columns([1,2,2,1])

        with fuck:
            st.markdown("<div></div>", unsafe_allow_html=True)

        with col1:
            st.markdown(getstarted, unsafe_allow_html=True)

        with col2:
            st.markdown(popular, unsafe_allow_html=True)
        
        with you: 
            st.markdown("<div></div>", unsafe_allow_html=True)

    

  
if __name__ == "__main__":
    home_page()