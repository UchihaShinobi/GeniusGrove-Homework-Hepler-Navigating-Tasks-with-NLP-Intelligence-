import streamlit as st
from datetime import datetime

def add_task(new_task, due_date, due_time):
    if new_task and due_date and due_time:
        due_datetime = datetime.combine(due_date, due_time)
        st.session_state.tasks.append({"task": new_task, "due_datetime": due_datetime, "completed": False})
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task, due date, and due time before adding.")

def display_task_list():
    st.subheader("Listed Tasks:")
    if not st.session_state.tasks:
        st.info("No tasks added yet. Add a new task above.")
    else:
        for i, task_info in enumerate(st.session_state.tasks, 1):
            task = task_info["task"]
            due_datetime = task_info["due_datetime"]
            completed = st.checkbox(f"{i}. {task} - Due: {due_datetime.strftime('%Y-%m-%d %H:%M')}", value=task_info["completed"], key=f"completed_{task}")

def remove_completed_tasks():
    st.session_state.tasks = [task_info for task_info in st.session_state.tasks if not task_info["completed"]]
    if not st.session_state.tasks:
        st.success("All completed tasks removed!")
    else:
        st.warning("No tasks selected. Please mark tasks as completed first.")

def clear_task_list():
    st.session_state.tasks = []
    st.success("Task list cleared!")

def main():
    st.header("Checklist✔️")

    # Initialize tasks using st.session_state
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    # Form for adding new tasks
    with st.form("task_form"):
        new_task = st.text_input("Add a new task:")
        due_date = st.date_input("Due Date")
        due_time = st.time_input("Due Time")
        add_button = st.form_submit_button("Add Task")

    if add_button:
        add_task(new_task, due_date, due_time)

    display_task_list()

    # Button to remove completed tasks
    if st.button("Remove Completed Tasks"):
        remove_completed_tasks()

    # Button to clear the entire task list
    if st.button("Clear Task List"):
        clear_task_list()

if __name__ == "__main__":
    main()
