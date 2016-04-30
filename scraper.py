import requests
from bs4 import BeautifulSoup

url = "https://beta.nightbot.tv/t/{channel}/commands".format(channel="curvyllama")
resp = requests.get(url=url)
data = resp.content
soup = BeautifulSoup(data, "html.parser")

for script in soup.find_all("script"):
    link = script.get("src")
    if link.startswith("scripts/app"):
        js = requests.get(url="https://beta.nightbot.tv/"+link)
        js_data = js.content
        js_soup = BeautifulSoup(js_data, "html.parser")
        print js_soup
