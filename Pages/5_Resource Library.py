import streamlit as st
import time

# Dictionary representing NCERT books for different classes and subjects
ncert_books = {
    "Class 1": {
        "Mathematics": "Class 1 Mathematics NCERT Book",
        "Science": "Class 1 Science NCERT Book",
    },
    "Class 2": {
        "Mathematics": "Class 2 Mathematics NCERT Book",
        "Science": "Class 2 Science NCERT Book",
    },
    "Class 3": {
        "Mathematics": "Class 3 Mathematics NCERT Book",
        "Science": "Class 3 Science NCERT Book",
    },
    "Class 4": {
        "Mathematics": "Class 4 Mathematics NCERT Book",
        "Science": "Class 4 Science NCERT Book",
    },
    "Class 5": {
        "Mathematics": "Class 5 Mathematics NCERT Book",
        "Science": "Class 5 Science NCERT Book",
    },
    "Class 6": {
        "Mathematics": "Class 6 Mathematics NCERT Book",
        "Science": "Class 6 Science NCERT Book",
    },
    "Class 7": {
        "Mathematics": "Class 7 Mathematics NCERT Book",
        "Science": "Class 7 Science NCERT Book",
    },
    "Class 8": {
        "Mathematics": "Class 8 Mathematics NCERT Book",
        "Science": "Class 8 Science NCERT Book",
    },
    "Class 9": {
        "Mathematics": "Class 9 Mathematics NCERT Book",
        "Science": "Class 9 Science NCERT Book",
    },
    "Class 10": {
        "Mathematics": "Class 10 Mathematics NCERT Book",
        "Science": "Class 10 Science NCERT Book",
    },
    "Class 11": {
        "Mathematics": "Class 11 Mathematics NCERT Book",
        "Physics": "Class 11 Physics NCERT Book",
        "Chemistry": "Class 11 Chemistry NCERT Book",
        "Biology": "Class 11 Biology NCERT Book",
    },
    "Class 12": {
        "Mathematics": "Class 12 Mathematics NCERT Book",
        "Physics": "Class 12 Physics NCERT Book",
        "Chemistry": "Class 12 Chemistry NCERT Book",
        "Biology": "Class 12 Biology NCERT Book",
    },
    # Add more classes and subjects as needed
}

# Dictionary representing links for NCERT books
ncert_links = {
    "Class 1 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?aejm1=0-13",
    "Class 1 Science NCERT Book": "https://www.tiwariacademy.com/ncert-solutions/class-1/science/",
    "Class 2 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?bejm1=0-11",
    "Class 2 Science NCERT Book": "https://www.tiwariacademy.com/ncert-solutions/class-2/science/",
    "Class 3 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?cemh1=0-14",
    "Class 3 Science NCERT Book": "https://www.tiwariacademy.com/ncert-solutions/class-3/science/",
    "Class 4 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?demh1=0-14",
    "Class 4 Science NCERT Book": "https://www.studyadda.com/notes/4th-class/35/science/5",
    "Class 5 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?eemh1=0-14",
    "Class 5 Science NCERT Book": "https://byjus.com/cbse/class-5-science/",
    "Class 6 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?femh1=0-12",
    "Class 6 Science NCERT Book": "https://byjus.com/ncert-solutions-class-6-science/",
    "Class 7 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?gemh1=0-13",
    "Class 7 Science NCERT Book": "https://ncert.nic.in/textbook.php?gemh1=0-13",
    "Class 8 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?hemh1=0-13",
    "Class 8 Science NCERT Book": "https://ncert.nic.in/textbook.php?hesc1=0-13",
    "Class 9 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?iemh1=0-12",
    "Class 9 Science NCERT Book": "https://ncert.nic.in/textbook.php?iesc1=0-12",
    "Class 10 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?jemh1=0-14",
    "Class 10 Science NCERT Book": "https://ncert.nic.in/textbook.php?jesc1=0-13",
    "Class 11 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?kemh1=0-14",
    "Class 11 Physics NCERT Book": "https://ncert.nic.in/textbook.php?keph1=0-7",
    "Class 11 Chemistry NCERT Book": "https://ncert.nic.in/textbook.php?kech1=0-6",
    "Class 11 Biology NCERT Book": "https://ncert.nic.in/textbook.php?kebo1=0-19",
    "Class 12 Mathematics NCERT Book": "https://ncert.nic.in/textbook.php?lemh1=0-6",
    "Class 12 Physics NCERT Book": "https://ncert.nic.in/textbook.php?leph1=0-8",
    "Class 12 Chemistry NCERT Book": "https://ncert.nic.in/textbook.php?lech1=0-5",
    "Class 12 Biology NCERT Book": "https://ncert.nic.in/textbook.php?lebo1=0-13",
    # Add more links as needed
}

# Streamlit app
def main():
    st.header("NCERT Book Resource Library📚")

    # Dropdown to select class
    selected_class = st.selectbox("Select Class", list(ncert_books.keys()))

    # Dropdown to select subject based on the selected class
    selected_subject = st.selectbox(
        "Select Subject", list(ncert_books[selected_class].keys())
    )

    # Display the selected NCERT book with animation
    with st.spinner("Loading..."):
        time.sleep(2)  # Simulate loading time

    # Check if the selected book has a corresponding link
    if ncert_books[selected_class][selected_subject] in ncert_links:
        # Display link button with emoji
        if st.button("Open Link 🌐", key="link_button"):
            st.success(f"👉 Opening link: {ncert_links[ncert_books[selected_class][selected_subject]]}")

if __name__ == "__main__":
    main()
