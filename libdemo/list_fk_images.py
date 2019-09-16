from bs4 import BeautifulSoup
import requests

resp = requests.get("https://www.flipkart.com")

soup = BeautifulSoup(resp.text, "lxml")  # html parser by lxml
for image in soup.find_all("img"):
    if 'src' in image.attrs:
        print(image['src'])
