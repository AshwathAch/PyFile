import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the input field
url = 'https://example.com/page_with_input_field'

# Send a GET request to fetch the HTML content of the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the input field by its placeholder attribute
    input_field = soup.find('input', {'placeholder': 'Mobile Number'})

    # Check if the input field is found
    if input_field:
        # Extract the logic name or identifier (if available)
        logic_name = input_field.get('name')

        # Print the logic name
        print("Logic name:", logic_name)
    else:
        print("Input field not found.")
else:
    print("Failed to fetch webpage. Status code:", response.status_code)
