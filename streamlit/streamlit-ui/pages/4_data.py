import streamlit as st
import requests

# Set up the Streamlit page
st.title("Product Data from DummyJSON API")
st.write("This app fetches and displays product data from the DummyJSON API.")

# Define the API URL
url = "https://dummyjson.com/products"

# Add a button to fetch data
if st.button("Fetch Data"):
    # Show a spinner while loading data
    with st.spinner("Fetching data..."):
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            products = data.get("products", [])
            
            # Display the list of products
            st.subheader("Products:")
            for product in products:
                st.write(f"**Product Name**: {product['title']}")
                st.write(f"**Description**: {product['description']}")
                st.write(f"**Price**: ${product['price']}")
                st.write(f"**Category**: {product['category']}")
                st.image(product['thumbnail'], width=150)
                st.write("---")
        else:
            st.error("Failed to retrieve data from the API.")
