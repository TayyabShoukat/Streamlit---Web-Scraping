import streamlit as st

# Custom CSS for styling specific elements in Streamlit
st.markdown("""
    <style>
    /* Additional styling for a specific section */
    .custom-section {
        background-color: red;
        color: white !important;
        padding: 20px;
        border-radius: 50px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Content with title and styled text
st.markdown('<div class="custom-section"><h1>Styled Streamlit App</h1></div>', unsafe_allow_html=True)
st.write("This text and background color, depending on Streamlit's CSS behavior.")
text_contents=st.text_input("Favorite movie?")

# Download button for text content
st.download_button("Download some text", text_contents)

# Download button for an image file
with open("pic.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="pic.png",
        mime="image/png",
    )

# MIME stands for Multipurpose Internet Mail Extensions. It is a standard way of classifying file types on the internet. MIME types help browsers and email clients understand the nature and format of a file, enabling them to handle the file appropriately.

# For example:

# text/html for HTML files
# image/jpeg for JPEG images
# application/pdf for PDF files
# audio/mpeg for MP3 audio files


# Rating system using faces as a feedback option
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("faces")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
