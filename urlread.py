import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to scrape website and extract first row of the table
def scrape_table_first_row(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table element
    table = soup.find('table')
    
    # Extract the first row of the table
    first_row = table.find('tr')
    
    # Extract data from the cells of the first row
    data = []
    for cell in first_row.find_all('td'):
        data.append(cell.text.strip())
    
    return data

# Function to write content to Excel
def write_to_excel(data):
    df = pd.DataFrame(data, columns=['Content'])
    df.to_excel('table_first_row.xlsx', index=False)

# Main function
def main():
    url = 'https://example.com/table_page'  # Replace with the URL of the page containing the table
    
    while True:
        # Scrape table and extract first row
        first_row_data = scrape_table_first_row(url)
        
        # Write first row data to Excel
        write_to_excel({'Content': first_row_data})
        
        # Wait for 3 minutes
        time.sleep(180)

if __name__ == "__main__":
    main()
