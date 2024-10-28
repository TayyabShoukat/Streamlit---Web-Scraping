import streamlit as st
import requests

# Set up the Streamlit page
# Function to reset session state
def reset_app():
    st.session_state.clear()

# Set up the Streamlit page
if st.button("Reset"):
    reset_app()
    
    
    
    
    
    
    
    
    
st.title("*Product* Data from DummyJSON API")
st.write("This app fetches and displays product data from the DummyJSON API.")
st.page_link("pages/2_todo.py",label="Todo Page")
# Define the API URL
url = "https://fakestoreapi.com/products?limit=5"

# Display option for view type
view_type = st.radio("Choose Display Type:", ("List View", "Grid View"))
# Add a button to fetch data
if st.button("Fetch Data"):
    # Show a spinner while loading data and store data in session state
    with st.spinner("Fetching data..."):
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            st.session_state["products"] = response.json()
            st.session_state["data_fetched"] = True
        else:
            st.error("Failed to retrieve data from the API.")
            st.session_state["data_fetched"] = False

# Display products only if data has been fetched
if st.session_state.get("data_fetched"):
    products = st.session_state["products"]
    
    st.subheader("Products:")
    if view_type == "List View":
        # List view display
        for product in products:
            st.write(f"**Product Name**: {product['title']}")
            st.write(f"**Description**: {product['description']}")
            st.write(f"**Price**: ${product['price']}")
            st.write(f"**Category**: {product['category']}")
            st.image(product['image'], width=150)
            st.write("---")
    
    elif view_type == "Grid View":
        # Grid view display
        cols = st.columns(3)  # 3 columns for a grid layout
        for id, product in enumerate(products):
            with cols[id % 3]:
                st.image(product['image'])
                st.write(f"**{product['title']}**")
                st.write(f"Price: ${product['price']}")
                st.write(f"Category: {product['category']}")
                st.write(f"description: {product['description']}")
