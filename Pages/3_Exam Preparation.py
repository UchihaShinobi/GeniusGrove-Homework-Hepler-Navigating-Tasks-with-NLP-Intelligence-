import streamlit as st
import time

def redirect_link(grade, subject):
    links = {
        "8": {"Maths": "https://byjus.com/cbse-sample-paper-class-8-maths-set-1/", "Science": "https://byjus.com/cbse-sample-paper-class-8-science-set-1/"},
        "9": {"Maths": "https://byjus.com/cbse-sample-papers-for-class-9-maths/", "Science": "https://byjus.com/cbse-sample-papers-for-class-9-science-set-1/"},
        "10": {"Maths": "https://cbseacademic.nic.in/web_material/SQP/ClassX_2023_24/MathsStandard-SQP.pdf", "Science": "https://cbseacademic.nic.in/web_material/SQP/ClassX_2022_23/Science-SQP.pdf"},
        "11": {"Physics": "https://byjus.com/cbse-sample-papers-class-11-physics-set-1/", "Chemistry": "https://byjus.com/cbse-sample-papers-class-11-chemistry-set-1-solution/", "Maths": "https://byjus.com/cbse-sample-papers-class-11-maths-set-1/"},
        "12": {"Physics": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2022_23/Physics-SQP.pdf", "Chemistry": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/Chemistry-SQP.pdf", "Maths": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2022_23/Maths-SQP.pdf"},
    }

    grade_str = str(grade)
    if grade_str in links and subject in links[grade_str]:
        return links[grade_str][subject]
    else:
        return None

def main():
    st.header("Question Material📒")

    # Grade selection dropdown
    grade_options = ["Select Grade", "8", "9", "10", "11", "12"]
    grade = st.selectbox("Select Grade:", grade_options)

    # Subject selection dropdown
    subjects_grade_8_to_10 = ["Select Subject", "Maths", "Science"]
    subjects_grade_11_and_12 = ["Select Subject", "Physics", "Chemistry", "Maths"]

    if grade in ["8", "9", "10"]:
        subject_options = subjects_grade_8_to_10
    elif grade in ["11", "12"]:
        subject_options = subjects_grade_11_and_12
    else:
        subject_options = ["Select Subject"]

    subject = st.selectbox("Select Subject:", subject_options)

    if st.button("Get Question Material"):
        with st.spinner("Fetching question material..."):
            time.sleep(2)  # Simulating some processing time

            if grade != "Select Grade" and subject != "Select Subject":
                link = redirect_link(grade, subject)
                if link:
                    st.success(f"Click [here]({link}) to access the question material.")
                else:
                    st.error("Invalid Grade or Subject selected.")
            else:
                st.warning("Please select both Grade and Subject.")

if __name__ == "__main__":
    main()
