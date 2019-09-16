from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com")

soup = BeautifulSoup(resp.text, "lxml")
table = soup.find("table", id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")
for tr in rows[1:]:
    cols = tr.find_all("td")
    print(f"{cols[0].text:50s} {cols[2].text}")
