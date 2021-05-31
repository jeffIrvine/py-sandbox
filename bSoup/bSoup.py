import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://secretlab.co/collections"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify())

# images = soup.find_all("img")

# number = 0

# for image in images:
#   image_src = image["src"]
#   print(image_src)
#   urllib.request.urlretrieve(image_src)
#   number += 1