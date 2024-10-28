import streamlit as st

# Initialize session state for tasks
if 'tasks_list' not in st.session_state:  # Changed 'tasks' to 'tasks_list'
    st.session_state['tasks_list'] = []  # Initialize as a list

# Title and input box for new tasks
st.title("Basic To-Do App")
new_task = st.text_input("Enter a new task:", "")

# Add a new task
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks_list.append(new_task)
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task before adding.")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.tasks_list:
    for i, task in enumerate(st.session_state.tasks_list):
        col1, col2 = st.columns([8, 1])
        col1.write(f"{i + 1}. {task}")
        # Delete task button
        if col2.button("Delete", key=i):
            st.session_state.tasks_list.pop(i)
else:
    st.write("No tasks yet!")
