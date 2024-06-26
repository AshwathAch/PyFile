import requests

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            data = response.json()
            return data.get('origin')
        else:
            print("Failed to retrieve public IP:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print("Your public IP address is:", public_ip)
    else:
        print("Failed to retrieve your public IP address.")
