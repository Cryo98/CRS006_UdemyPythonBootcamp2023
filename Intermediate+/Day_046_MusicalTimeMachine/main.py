import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.billboard.com/charts/hot-100/"

date_string = input("To which time do you want to travel? (Pst, use the format YYYY-MM-DD): ")
response = requests.get(BASE_URL + date_string)

soup = BeautifulSoup(response.content, "html.parser")

song_titles = soup.select("li.o-chart-results-list__item > h3#title-of-a-story")
for title in song_titles:
    print(f"{title.getText().strip()}")
