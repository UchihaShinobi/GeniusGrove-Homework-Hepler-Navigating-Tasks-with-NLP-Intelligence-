import streamlit as st

st.header("Get In Touch With Me!:mailbox:")

contact_form = """
<form action="https://formsubmit.co/makarandmahajan111@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    file_path = "D:\\Data Scientist\\Projects\\GeniusGrove\\Pages\\style\\style.css"
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Could not find CSS file at path: {file_path}")

local_css("style.css")
