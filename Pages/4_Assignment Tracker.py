import streamlit as st
import pandas as pd
from datetime import datetime

# Load existing assignments or create a new DataFrame
file_path = "assignments.csv"

csv_file = st.file_uploader("Upload CSV", type=["csv"], key="csv_upload")
if csv_file is not None:
    # If a CSV file is uploaded, use it
    uploaded_df = pd.read_csv(csv_file)
    st.subheader("CSV File Preview:")
    st.dataframe(uploaded_df.head())
else:
    # If no file is uploaded, check if the CSV file already exists
    try:
        assignments_df = pd.read_csv(file_path)
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame
        assignments_df = pd.DataFrame(columns=['Subject', 'Description', 'Due Date', 'Status'])

    # Streamlit App
    st.header("Task Monitor⏰")

    # Add Assignment Section
    subject = st.text_input("Assign Task")
    description = st.text_area("Description")
    due_date = st.date_input("Due Date", min_value=datetime.now())
    add_button = st.button("Assign Task")

    # Add assignment to DataFrame
    if add_button:
        assignments_df = pd.concat([assignments_df, pd.DataFrame({
            'Subject': [subject],
            'Description': [description],
            'Due Date': [due_date],
            'Status': ['Not Completed']
        })], ignore_index=True)

    # Display Assignments
    st.header("Assignments Dues")
    st.table(assignments_df)

    # Update Assignment Status Section
    st.header("Update Assignment Status")
    selected_assignment = st.selectbox("Select Assignment", assignments_df['Subject'])
    status_options = ['Not Completed', 'Completed']
    update_status = st.radio("Update Status", status_options, index=status_options.index('Not Completed'))
    update_button = st.button("Update Status")

    # Update assignment status in DataFrame
    if update_button:
        assignments_df.loc[assignments_df['Subject'] == selected_assignment, 'Status'] = update_status

    # Save the DataFrame to a CSV file
    assignments_df.to_csv(file_path, index=False)
