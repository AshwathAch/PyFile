import pyautogui
import time

# Function to take a screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')  # Save the screenshot to a file

# Function to click at a specific point
def click_at(x, y):
    pyautogui.click(x, y)

# Example usage
if __name__ == "__main__":
    # Take a screenshot
    take_screenshot()

    # Wait for a few seconds (adjust the time as needed)
    time.sleep(3)

    # Click at a specific point (replace these coordinates with your desired point)
    click_at(500, 300)  # Example coordinates (x, y)
