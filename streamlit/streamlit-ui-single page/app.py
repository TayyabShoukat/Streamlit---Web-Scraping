import streamlit as st
import pandas as pd

# Header
# st.header("Welcome to My App")

# st.text("# This is plain text, not a heading")
# st.text("**Bold text** and *italic text* won’t work here.")

# st.markdown("# Heading 1") 
# st.markdown("## Heading2") 
# st.markdown("**bold text**")
# st.markdown("`code`")
# st.markdown("**Bold text** and *italic text*.")
# st.markdown("1. Item one\n2. Item two")




# # Subheader
# st.subheader("Please enter your information below")

# # Textbox
# name = st.text_input("Enter your name:")

# # Display the entered name
# if name:
#     st.write(f"Hello, {name}!")

# # Adding title of your app
# st.title('Single Page App')

# # adding simple text
# st.write('Here is a simple text')

# # user input
# number = st.slider('Pick a number', 0, 100, 10)

# # print the text of number
# st.write(f'You selected: {number}')

# # adding a button
# if st.button('Greeting'):
#     st.write('Hi, hello there')
# else:
#     st.write('Goodbye')

# # add radio button with options
# genre = st.radio(
#     "What's your favorite movie genre",
#     ('Comedy', 'Drama', 'Documentary'))

# # print the text of genre
# st.write(f'You selected: {genre}')



# st.image("image/sirnaveed.jpg", caption="Sir Naveed", width=300)



# add a drop down list on the left sidebar
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

# add your whatsapp number
st.sidebar.text_input('Enter your Name')

# # add a file uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# # create a line plot
# # Plotting
# # Create a DataFrame
data = pd.DataFrame({
  'first column': list(range(1, 11,1)),    # adjust to range 1 to 10
  'second column': list(range(2, 22, 2)),  # Adjusted to range 2 to 20
  'Third column': list(range(3, 33, 3)),  # Adjusted to range 3 to 30
  'Fourth column': [x ** 2 for x in range(1, 11)]
})

# Display the line chart
st.line_chart(data)


# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "City": ["New York", "San Francisco", "Chicago"]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Display the table in the app
st.dataframe(df)

# Convert DataFrame to CSV
csv_data = df.to_csv(index=False)

# Download button
st.download_button(
    label="Download data as CSV",
    data=csv_data,
    file_name="table_data.csv",
    mime="text/csv",
)
