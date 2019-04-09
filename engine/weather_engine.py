import requests
from bs4 import BeautifulSoup as bs
import sys

city = sys.argv[1]


def get_weather(place):
    place = place.replace(" ", "-")
    url = "https://www.weather-forecast.com/locations/" + place + "/forecasts/latest"
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    weather = soup.findAll("span", {"class": "phrase"})[0].text
    return weather

print(get_weather(city))
sys.stdout.flush()
