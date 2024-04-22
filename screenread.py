import pyautogui
import pytesseract
from PIL import Image
from openpyxl import Workbook

# Set the coordinates of the area you want to capture
x1, y1, width, height = 100, 100, 200, 100

# Capture the screen
screenshot = pyautogui.screenshot(region=(x1, y1, width, height))

# Save the screenshot to a file
screenshot.save("screenshot.png")

# Process the image if necessary (e.g., convert to grayscale)

# Perform OCR to extract text from the image
text = pytesseract.image_to_string(Image.open("screenshot.png"))

# Write the extracted text to an Excel file
wb = Workbook()
ws = wb.active
ws.append([text])

# Save the Excel file
wb.save("output.xlsx")
