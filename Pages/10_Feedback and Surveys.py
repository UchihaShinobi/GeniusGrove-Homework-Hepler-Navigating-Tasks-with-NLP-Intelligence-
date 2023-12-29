import streamlit as st
import pandas as pd

def collect_feedback():
    st.header("Student Feedback Form📝")

    name = st.text_input("Name:")
    email = st.text_input("Email:")

    st.subheader("Feedback")
    satisfaction = st.slider("How satisfied are you with the course? (1-10)", 1, 10)
    comments = st.text_area("Comments:")

    feedback_data = pd.DataFrame({
        "Name": [name],
        "Email": [email],
        "Satisfaction": [satisfaction],
        "Comments": [comments]
    })

    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

        feedback_data.to_csv("feedback_data.csv", mode="a", index=False, header=not st.session_state.get("file_exists", False))
        st.session_state["file_exists"] = True

def main():
    collect_feedback()

if __name__ == "__main__":
    main()
