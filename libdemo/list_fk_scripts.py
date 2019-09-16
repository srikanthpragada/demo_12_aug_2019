from bs4 import BeautifulSoup
import requests

resp = requests.get("https://www.flipkart.com")

soup = BeautifulSoup(resp.text, "lxml")  # html parser by lxml
for script in soup.find_all("script"):
    if 'src' in script.attrs:
        print(script['src'])
