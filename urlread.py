import requests
from bs4 import BeautifulSoup
import time

def login_to_website(username, password):
    # Perform login (replace with actual login logic)
    session = requests.session()
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post('https://example.com/login', data=login_data)
    return session

def extract_information(session):
    # Extract information from the webpage (replace with actual scraping logic)
    response = session.get('https://example.com/dashboard')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table containing the data
    table = soup.find('table', class_='your_table_class')  # Replace 'your_table_class' with the actual class of the table
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
    # Replace 'username' and 'password' with actual login credentials
    username = 'your_username'
    password = 'your_password'
    
    while True:
        session = login_to_website(username, password)
        information = extract_information(session)
        write_to_file(information)
        print('Information written to file:', information)
        time.sleep(180)  # 3 minutes (180 seconds)
