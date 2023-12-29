import streamlit as st
from datetime import datetime

# Initialize session state to store chat messages
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []

# Streamlit App
st.header("ChitChat Thread💭")

# User input for username
username = st.text_input("User Alias:")

# User input for messages
user_input = st.text_area("Compose Note:")

# File upload option
uploaded_file = st.file_uploader("Upload file", type=["csv", "txt", "pdf"])

# Button to send messages
send_button = st.button("Send")

if send_button and user_input:
    # Add the user's message to the shared chat_messages list
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.chat_messages.append(f"[{timestamp}] {username}: {user_input}")

# Display the chat messages with rounded bars
st.text("Chat Messages:")
for message in st.session_state.chat_messages:
    st.markdown(
        f"""<div style="background-color:#4CAF50; color: black; border-radius: 10px; padding: 10px; margin: 5px;">
            {message}
        </div>""",
        unsafe_allow_html=True
    )

# Display uploaded file
if uploaded_file:
    st.text("Uploaded File:")
    st.write(uploaded_file)
