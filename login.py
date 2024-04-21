import requests
import webbrowser

def login_and_open_page(username, password):
    # Send login credentials
    login_data = {
        'username': username,
        'password': password
    }
    login_url = 'https://example.com/login'  # Replace with the actual login URL
    response = requests.post(login_url, data=login_data)

    # Check if login was successful
    if response.status_code == 200:
        # Open the next page in Firefox
        next_page_url = 'https://example.com/next_page'  # Replace with the actual URL of the next page
        webbrowser.get('firefox').open(next_page_url)  # Open in Firefox

        print("Login successful. Opening next page in Firefox.")
    else:
        print("Login failed.")

if __name__ == '__main__':
    # Replace 'username' and 'password' with actual login credentials
    username = 'your_username'
    password = 'your_password'

    login_and_open_page(username, password)
