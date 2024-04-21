import requests
from bs4 import BeautifulSoup
import time

def extract_information():
    # Extract information from the webpage (replace with actual scraping logic)
    response = requests.get('https://example.com/dashboard')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the division (div) with class name "parity"
    target_div = soup.find('div', class_='parity')  # Replace 'parity' with the actual class name of the division
    # Find the table within the division
    table = target_div.find('table')  # This will find the first table within the division
    # Find all rows in the table body (tbody) except the first one (skipping the header)
    rows = table.find('tbody').find_all('tr')[1:]
    # Extract the text from the first row
    first_row = rows[0].text.strip()
    return first_row

def write_to_file(information):
    # Write extracted information to a file
    with open('information.txt', 'a') as file:
        file.write(information + '\n')

if __name__ == '__main__':
    while True:
        information = extract_information()
        write_to_file(information)
        print('Information written to file:', information)
        time.sleep(180)  # 3 minutes (180 seconds)
