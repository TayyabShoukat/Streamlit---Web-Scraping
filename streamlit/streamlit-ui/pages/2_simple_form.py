import streamlit as st

name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter your Father Name : ")
adr = st.text_area("Enter Your Text : ")
classLevel = st.selectbox("Enter Your Class :", (1, 2, 3, 4, 5, 6))

button = st.button("Done")
if button:
    st.markdown(f"""
    Name: {name}  
    Father Name: {fname}  
    Address: {adr}  
    Class: {classLevel}
    """)


