import streamlit as st

def how_to_use():
    how_to_html = """\
        <div style="
            padding: 5px 10px; 
            text-align: center; 
            max-width: 50%; 
            margin: 0 auto 20px auto;
            border-radius: 22px;
            background-color: {};
            ">
            <h1>How to Use</h1>
            <p>1. Enable your webcam</p>
            <p>2. Use hand gestures to navigate through the recipes</p>
            <p>3. Enjoy cooking without touching your device!</p>
        </div>
    """.format(st.get_option("theme.secondaryBackgroundColor"))

    st.markdown(how_to_html, unsafe_allow_html=True)


if __name__ == "__main__":
    how_to_use()