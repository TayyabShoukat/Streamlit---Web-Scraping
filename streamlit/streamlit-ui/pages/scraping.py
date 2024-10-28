import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_population_data():
    # Define the URL of the Wikipedia page we want to scrape
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    # Make a GET request to fetch the raw HTML content
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table containing population data
    table = soup.find('table', {'class': 'wikitable'})
    if not table:
        return pd.DataFrame()  # Return an empty DataFrame if no table is found

    # Extract table headers
    headers = [header.text.strip() for header in table.find_all('th')]

    # Extract table rows
    rows = []
    for row in table.find_all('tr')[1:]:
        columns = [col.text.strip() for col in row.find_all(['td', 'th'])]
        if len(columns) == len(headers):
            rows.append(columns)
    
    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df

def main():
    st.title("World Population Data Scraper")
    st.write("This app scrapes the latest population data of countries from Wikipedia.")
    
    # Scrape the data
    if st.button("Scrape Data"):
        st.write("Fetching data...")
        df = scrape_population_data()
        
        if not df.empty:
            st.success("Data fetched successfully!")
            st.dataframe(df)
        else:
            st.error("No data found. The website structure might have changed.")
    
if __name__ == "__main__":
    main()
