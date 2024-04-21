from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def extract_information():
    # Create a Selenium WebDriver instance
    driver = webdriver.Firefox(executable_path='/path/to/geckodriver')  # Replace '/path/to/geckodriver' with the actual path to geckodriver
    
    # Load the webpage
    driver.get('https://example.com/dashboard')
    time.sleep(5)  # Allow time for JavaScript to execute and content to load
    
    # Find the division (div) with class name "parity"
    target_div = driver.find_element(By.CLASS_NAME, 'parity')  # Replace 'parity' with the actual class name of the division
    # Find the table within the division
    table = target_div.find_element(By.TAG_NAME, 'table')  # This will find the first table within the division
    # Find all rows in the table body (tbody) except the first one (skipping the header)
    rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
    # Extract the text from the first row
    first_row = rows[0].text.strip()
    
    # Close the WebDriver
    driver.quit()
    
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
