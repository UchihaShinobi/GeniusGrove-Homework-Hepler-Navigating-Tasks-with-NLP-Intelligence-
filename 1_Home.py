import json
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GeniusGrove", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# ---- LOAD ASSETS ----
lottie_coding = load_lottiefile("lottiefiles/homepage.json")

# ---- HEADER SECTION ----
with st.container():
    st.title("GeniusGrove♟️")
    st.subheader("Your Gateway to Comprehensive and Engaging Education")
    st.write("Education is the most powerful weapon which you can use to change the world. - Nelson Mandela")

# ---- LOTTIE ANIMATION BELOW THE PAGE CONTENT ----
with st.container():
    st_lottie(lottie_coding, height=600, width=800, key="coding")

# ---- COPYRIGHT, TERMS & CONDITIONS, PRIVACY POLICY ----
with st.container():
    st.write("""
    © 2023 GeniusGrove. All rights reserved. | 
    [Terms & Conditions](#) | 
    [Privacy Policy](#)
    """)
