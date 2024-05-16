import requests
from bs4 import BeautifulSoup
import os

# Set the URL and the folder path
url = "https://m.blog.naver.com/worldforsale/223433717053?referrerCode=1"
folder_path = "Download"

# Check if the folder exists, create it if not
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Send a GET request to the URL and get the HTML response
response = requests.get(url)
html = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all image tags on the page
image_tags = soup.find_all('img')

# Download each image and save it in the folder
for img_tag in image_tags:
    img_url = img_tag.get('src')
    if img_url:
        # Send a GET request to the image URL and get the image content
        response = requests.get(img_url)
        img_content = response.content

        # Save the image in the folder
        with open(os.path.join(folder_path, os.path.basename(img_url)), 'wb') as f:
            f.write(img_content)

print("Images downloaded successfully!")

# This code is proposed for mission execution
# This code will be run in /Users/alex
# This code file is actually located at /Users/alex/.aiexe_venv/20240512_131114_981.py and you can review the code by opening this file.
# Additional code included at the top of this file ensures smooth operation. For a more detailed review, it is recommended to open the actual file.
# Please review the code carefully as it may cause unintended system behavior