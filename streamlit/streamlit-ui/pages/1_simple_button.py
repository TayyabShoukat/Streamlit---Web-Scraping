import streamlit as st

st.header("Buttons")

# Regular button with session state tracking
if 'hello_world_clicked' not in st.session_state:
    st.session_state['hello_world_clicked'] = False

if st.button("Hello World", type="secondary"):
    st.session_state['hello_world_clicked'] = not st.session_state['hello_world_clicked']
st.write("Hello World clicked:", st.session_state['hello_world_clicked'])

# # Unsustained output button
if 'unsustained_output' not in st.session_state:
    st.session_state['unsustained_output'] = False

if st.button("Check Output"):
    st.session_state['unsustained_output'] = not st.session_state['unsustained_output']
st.write("Unsustained Output clicked:", st.session_state['unsustained_output'])

# # Sustained buttons with unique states
if 'button_2_state' not in st.session_state:
    st.session_state['button_2_state'] = None

if st.button("Check output 2 of sustained button"):
    st.session_state['button_2_state'] = "Button 2 clicked!"

if 'button_3_state' not in st.session_state:
    st.session_state['button_3_state'] = None

if st.button("Check output 3 of sustained button"):
    st.session_state['button_3_state'] = "Button 3 clicked"

# Display the states of button 2 and button 3
st.write("Button 2 state:", st.session_state['button_2_state'])
st.write("Button 3 state:", st.session_state['button_3_state'])

# Say hello button with toggle state
if 'say_hello_clicked' not in st.session_state:
    st.session_state['say_hello_clicked'] = False

if st.button("Say hello"):
    st.session_state['say_hello_clicked'] = not st.session_state['say_hello_clicked']

if st.session_state['say_hello_clicked']:
    st.write("Why hello there")
else:
    st.write("Goodbye")

# Reset button to clear session states
if st.button("Reset", type="primary"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# Display current session state
st.write("Current Session State:")
st.write(st.session_state)
